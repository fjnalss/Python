from .models import Sam, Config


def oho_url(domain):
    rulejson = Sam.objects.filter(domain=domain).values_list('rulejson', flat=True)
    config = ""
    for rule in rulejson:
        rule_dict = eval(rule)  # 需要将数据库的转换成dict才可以进行循环
        for item in rule_dict:
            if "actionid" in item:
                config = "http头域: "+ item['h'] + "\n" + "http头域值：" + item['value']
            if "conditionid" in item:
                config = config + "\n" + "URL匹配模式：" + item['m']
        Config.objects.create(domain=domain, config=config)
