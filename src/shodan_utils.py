from shodan import Shodan, APIError
import time

def get_vuln(CVE_CODE, API_KEY):
    search_query = CVE_CODE
    api = Shodan(API_KEY)
    
    # Scrape all pages
    all_results = []
    page = 1
    while True:
        try:
            results = api.search(search_query, page=page)
            if page == 1: print(f"[*] Total possible results: {results['total']}")
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
                print(f"[*] Retrieved {len(results['matches'])} results from page {page}...")
            else:
                print(f"[*] Retrieved all results from page {page}...")
            
            # No more pages left...
            if len(results['matches']) < 100:
                break

            page += 1
            
            # Don't fuck with the rate-limit!
            time.sleep(1)
        except API_KEY as err:
            print(f"[!] Shodan API Error: {err}")
            break
    print(f"[*] Done browsing all pages for '{search_query}'...")
    print(f"[*] Total results for '{search_query}': {len(all_results)} ...")
    return all_results
    
            
    