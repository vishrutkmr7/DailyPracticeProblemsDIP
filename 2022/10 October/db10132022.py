"""
This question is asked by Google.
Email addresses are made up of local and domain names.
For example in kevin@dailybyte.com, kevin is the local name and dailybyte.com is the domain name.
Email addresses may also contain '+' or '.' characters besides lowercase letters. If there is a '.'
in the local name of the email address it is ignored. Everything after a '+' in the local name is also ignored.
For example ke.vin+abc@dailybyte.com is equivalent to kevin@dailybyte.com Given a list of email addresses,
find the number of unique addresses.

Ex: Given the following emails...

emails = [
    "test.email+kevin@dailybyte.com",
    "test.e.mail+john.smith@dailybyte.com",
    "testemail+david@daily.byte.com"
], return 2. "testemail@dailybyte.com" and "testemail@daily.byte.com" are unique since the first two email addresses in the list are equivalent.
"""


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            unique_emails.add(f"{local}@{domain}")
        return len(unique_emails)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.numUniqueEmails(
            [
                "test.email+kevin@dailybyte.com",
                "test.e.mail+john.smith@dailybyte.com",
                "testemail+david@daily.byte.com",
            ]
        )
        == 2
    )
    print("All tests passed.")
