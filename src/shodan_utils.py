from shodan import Shodan, APIError
import time

def get_vuln(CVE_CODE, API_KEY, API_DELAY):
    search_query = "vuln:" + CVE_CODE + ' country:"DE" port:8080'
    api = Shodan(API_KEY)
    
    # Scrape all pages
    all_results = []
    page = 1
    while True:
        try:
            results = api.search(search_query, page=page)
            if page == 1:
                print(f"\n[*] Total possible results: {results['total']}")
                print(f"[*] Total possible pages: {round(int(results['total']) / 100, 1)}")
                print(f"[*] Estimated cost: {round(int(results['total']) / 100, 0)} credits")
                continue_question = input("Continue with action? (y/n)  ")
                if continue_question == "n":
                    print(f"[!] Aborted execution")
                    return
                print("[*] Beginning to scrape \n")
                
            print(f"[*] Page: {page}")
            
            # Page empty; break the loop
            if 'matches' not in results or len(results['matches']) == 0:
                if page == 1:
                    print("[!] No results were found...")
                else: 
                    print("[!] No results were found for current page...")                
                break
            
            all_results.extend(results)
            if not len(results['matches']) == 100:
                print(f"[*] Retrieved {len(int(results['matches']))} results from page {page}...")
            else:
                print(f"[*] Retrieved all results from page {page}...")
            
            # No more pages left...
            if len(results['matches']) < 100:
                break

            page += 1
            
            time.sleep(int(API_DELAY)) 
            print(f"[*] Waiting {str(API_DELAY)} seconds")
        except APIError as err:
            print(err)
            print(f"[!] Shodan API Error: {err}")
            break
    print(f"[*] Done browsing all pages for '{str(search_query).strip('vuln:')}'...")
    print(f"[*] Total results for '{search_query}': {len(all_results)} ...")
    return all_results
    
            
    