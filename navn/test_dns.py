import dnshandler

dns = dnshandler.DNSHandler(
    "2001:470:e6fc:4000::4a11:aa",
    {
        "ssl.tallwireless.com.": (
            "gDzlZLznMSzqWOS1JmXEC7rqOiQ0cIyOVmDb1FRhx1UXPdjiZr0TOWhpso01UefoJxiz3xvSpg1XqC+7H3Bc8w==",
            "HMAC_MD5",
        )
    },
)

dns.add_host("testing.tallwireless.com", "128.92.32.23")
