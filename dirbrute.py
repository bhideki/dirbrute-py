import sys

import requests


def brute(url, wordlist):
    subdomain_test = []
    try:
        for word in wordlist:
            try:
                final_url = "{}/{}".format(url, word.strip())
                response = requests.get(final_url)
                code = response.status_code
                if code != 404:
                    print("{} -- {}".format(final_url, code))
                if code == 200:
                    subdomain_test.append(final_url)
                    for subdomain in subdomain_test:
                        for word in wordlist:
                            word = word.strip()
                            teste_final = "{}/{}".format(subdomain, word)
                            response2 = requests.get(teste_final)
                            if response2.status_code != 404:
                                print("{} --  {} ".format(teste_final,response2))
            except KeyboardInterrupt:
                sys.exit()
            except Exception as error:
                print(error)
                pass

    except KeyboardInterrupt:
        sys.exit()
    except Exception as error:
        print(error)
        pass

if __name__ == "__main__":
    url = sys.argv[1]
    wordlist = sys.argv[2]

    with open(wordlist, "r") as f:
        wordlist = f.readlines()
        brute(url, wordlist)

