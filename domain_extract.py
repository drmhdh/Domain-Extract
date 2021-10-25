def domain(url):
    domain = url.split("://", 1)[1].split("/", 1)[0]
    return domain
