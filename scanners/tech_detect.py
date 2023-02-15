import requests

def Detect(domain):

    debug = "[LOTUS] Framework Detected: "
    r = requests.get(f"https://{domain}/")
    if "vue" in r.text:
        print(debug, "Vue.js")
    if "svelte" in r.text:
        print(debug, "Svelte.js")
    elif "jquery"  in r.text:
        print(debug, "JQuery.js")
    elif "meteor" in r.text:
        print(debug, "Meteor.js")
    elif "next" in r.text:
        print(debug, "Next.js")
    else:
        pass

    re = requests.get(f"https://{domain}/.git/")
    if re.status_code != 404 or 403:
        print("[LOTUS] Detected: .git")

    rs = requests.get(f"https://{domain}/.env/")
    if re.status_code != 404 or 403:
        print("[LOTUS] Detected: .env")
