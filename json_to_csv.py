import json
url_list = []


def yield_json(final_dict,output_json):
    temp_list  = []
    temp_list.append(final_dict)
    with open(output_json, 'a') as outfile:
        for hostDict in temp_list:
            json.dump(hostDict, outfile)
            outfile.write('\n')

def prepare_data(single_json_line):
    data = ''
    for index in range(10):
        try:
            entity = single_json_line["Entity_" + str(index)]
            if(entity==""):
                continue
            else:
                data = data + entity + " "
        except:
            continue
    for index in range(10):

        try:
            labels = single_json_line["Labels_" + str(index)]
            if(labels==""):
                continue
            else:
                data = data + labels + " "
        except:
            continue
    return data

for index,line in enumerate(open("InnerJoin-Label-And-Entities-Output-4_5Million.json",'r',encoding="iso-8859-1")):
    f_single_row               = {}
    strip_line               = line.strip()
    stripped_single_line     = strip_line.strip()
    single_json_line         = json.loads(stripped_single_line)
    single_json_line         = dict(single_json_line)
    output                   = {}
    output['data']           = prepare_data(single_json_line)
    output['pt']             = single_json_line['Folder1']
    output['type']           = single_json_line['Folder2']
    output['url']            = single_json_line['URL']
    print(output)
    yield_json(output,"4_5million_entities_label_datatset.json")
    break;