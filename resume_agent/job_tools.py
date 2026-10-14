from ddgs import DDGS
from urllib.parse import urlparse


def search_company_jobs(company_name: str) -> dict:
    """
    Search for current job openings from the company's official careers site.

    Args:
        company_name: Name of the company whose jobs should be searched.

    Returns:
        A dictionary containing current job search results.
    """

    # Official career domains for companies we want to support.
    career_domains = {
        "apple": "jobs.apple.com",
        "google": "google.com/about/careers",
        "amazon": "amazon.jobs",
        "meta": "metacareers.com",
        "microsoft": "jobs.careers.microsoft.com",
        "nvidia": "nvidia.wd5.myworkdayjobs.com",
    }

    company_key = company_name.strip().lower()
    official_domain = career_domains.get(company_key)

    # Prefer the official careers website when we know it.
    if company_key == "apple":
        query = (
            'site:jobs.apple.com/en-us/details/ '
            '("Software Engineer" OR "Data Engineer" OR '
            '"Machine Learning Engineer" OR "AI Engineer")'
        )
    elif official_domain:
        query = f'site:{official_domain} "{company_name}" jobs'
    else:
        query = f'"{company_name}" official careers jobs'

    try:
        results = DDGS().text(
            query,
            max_results=15
        )

        jobs = []

        for result in results:
            title = result.get("title", "")
            url = result.get("href", "")
            description = result.get("body", "")

            if not url:
                continue

            # For known companies, only keep results from
            # the official careers domain.
            if official_domain:
                parsed_domain = urlparse(url).netloc.lower()
                base_domain = official_domain.split("/")[0].lower()

                if base_domain not in parsed_domain:
                    continue
            # For Apple, keep only individual job-detail pages.
            if company_key == "apple":
                if "/en-us/details/" not in url:
                    continue

            # Skip Apple jobs that appear to be expired or removed.
            if company_key == "apple":
                inactive_phrases = [
                    "does not exist",
                    "no longer available",
                    "role is no longer available",
                    "job is no longer available"
                ]

                description_lower = description.lower()

                if any(phrase in description_lower for phrase in inactive_phrases):
                    continue

            jobs.append({
                "title": title,
                "url": url,
                "description": description
            })
            

        return {
            "status": "success",
            "company": company_name,
            "official_domain": official_domain,
            "jobs_found": len(jobs),
            "jobs": jobs
        }

    except Exception as e:
        return {
            "status": "error",
            "company": company_name,
            "message": str(e),
            "jobs": []
        }