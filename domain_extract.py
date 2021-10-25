def domain(url):
    domain = url.split("://", 1)[1].split("/", 1)[0]
    return domain


def domains(urls):
    domains = []
    for url in urls:
        domains.append(domain(url))
    return domains
