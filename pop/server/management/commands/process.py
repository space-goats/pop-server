#!/usr/bin/env python3

from bs4 import BeautifulSoup as bs
from pprint import pprint

FILE = "linted.html"




def table_name(table):
    try:
        return table.previousSibling.text.strip()
    except:
        table_name.count += 1
        return "No Name {}".format(table_name.count)
# "static" variable for table_name
table_name.count = 0


def process_header_table(table):
    case_desc_dict = {}
    trs = table.findAll("tr")
    for tr in trs:
        tds = tr.findAll("td")
        td_set = []
        for td in tds:
            text = td.text.strip()
            if len(text) > 0:
                td_set.append(text)

        if len(td_set) > 1:
            name, lines = td_set
            case_desc_dict[name.replace(':', '')] = lines.split('\n')

    # TODO: these should each be further processed
    return case_desc_dict


def process_parties(table):
    parties = []
    ret = []
    last_party = None
    for tr in table.findChildren("tr"):
        tds = tr.findAll("td")
        if len(tds) < 5:  # skip the ones with no data
            continue

        if len(tds) == 6:
            last_party = tds

        if len(tds) == 5:
            # then it's an alias row
            parties.append((last_party, tds))

    for party_row, alias_row in parties:
        seq, assoc, end_date, type, id, name = party_row
        # clean them up, get text from the elements and strip it
        party_dict = {i: str.strip(j.text) 
                      for i, j in dict(seq=seq,
                                    assoc=assoc,
                                    end_date=end_date,
                                    type=type,
                                    id=id,
                                    name=name).items()}
    

        # grab the aliases
        _, _, _, _, aliases = alias_row
        a_stripped = aliases.text.strip()
        if a_stripped == 'none':
            a_stripped = None
        else:
            a_stripped = a_stripped.split('\n')

        party_dict['aliases'] = a_stripped

        ret.append(party_dict)

    return ret
        


def get_everything():

    with open(FILE, "rb") as f:
        soup = bs(f.read(), "html.parser")


    tables = soup.find_all("table")

    tmap = {table_name(t): t for t in tables}


    #pprint(tmap)
    #print(tmap.keys())

    main_case_info = process_header_table(tmap['Report Selection Criteria'])
    case_desc = process_header_table(tmap['Case Description'])
    parties = process_parties(tmap['Case Parties'])

    return {"main_case_info": main_case_info,
            "case_desc": case_desc,
            "parties": parties,
            }


def main():
    everything = get_everything()

    pprint(everything)

if __name__ == '__main__':
    main()
