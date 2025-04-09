import os
os.environ["OPENAI_API_KEY"] = 'xxx'
os.environ["SERPAPI_API_KEY"] = 'xxx'


import re
from agents.weibo_agent import lookup_V
from tools.general_tool import remove_non_chinese_fields
from tools.scraping_tool import get_data
from tools.textgen_tool import generate_letter


def find_bigV(flower: str) :

    response_UID = lookup_V(flower_type = flower )


    UID = re.findall(r'\d+', response_UID)[0]
    print("这位鲜花大V的微博ID是", UID)


    person_info = get_data(UID)
    print(person_info)


    remove_non_chinese_fields(person_info)
    print(person_info)


    result = generate_letter(information = person_info)
    print(result)

    return result


if __name__ == "__main__":

    response_UID = lookup_V(flower_type = "牡丹" )


    UID = re.findall(r'\d+', response_UID)[0]
    print("这位鲜花大V的微博ID是", UID)


    person_info = get_data(UID)
    print(person_info)


    remove_non_chinese_fields(person_info)
    print(person_info)

    result = generate_letter(information = person_info)
    print(result)

    from flask import jsonify
    import json

    result = json.loads(result)
    abc = jsonify(
        {
            "summary": result["summary"],
            "facts": result["facts"],
            "interest": result["interest"],
            "letter": result["letter"],
        }
    ) 