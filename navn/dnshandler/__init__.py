import dns.query
import dns.update
import dns.tsigkeyring
import dns.tsig


class DNSHandler(object):
    def __init__(self, nameserver: str, tsigkeys: dict = None):
        self.nameserver = nameserver
        self.tsig_algo = dns.tsig.HMAC_MD5
        if tsigkeys is not None:
            self.keyring = dns.tsigkeyring.from_text(
                {k: v[0] for k, v in tsigkeys.items()}
            )
        else:
            self.keyring = None

    def add_host(self, hostname, ip):
        update = dns.update.Update(
            "tallwireless.com", keyring=self.keyring, keyalgorithm=dns.tsig.HMAC_MD5
        )
        update.add(hostname, 3600, "A", ip)
        print(update)
        try:
            print(dns.query.tcp(update, self.nameserver))
        except Exception as e:
            print(e)
        return 0

    def update_host(self, hostname, ip):
        update = dns.update.Update(
            "tallwireless.com", keyring=self.keyring, keyalgorithm=self.tsig_algo
        )
        update.update(hostname, 3600, "A", ip)
        try:
            dns.query.tcp(update, self.nameserver)
        except Exception as e:
            print(e)
        return 0

    def delete_host(self, hostname, ip):
        update = dns.update.Update(
            "tallwireless.com", keyring=self.keyring, keyalgorithm=self.tsig_algo
        )
        update.delete(hostname, 3600, "A", ip)
        try:
            dns.query.tcp(update, self.nameserver)
        except Exception as e:
            print(e)
        return 0
