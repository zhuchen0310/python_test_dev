#! /usr/bin/python
# -*- coding:utf-8 -*-

import json
import random
import bisect
import click


# 活动页 /activity
data = {
    'activity_info': {  # 活动相关信息
        'activity_time_string': '2018年5月1日—2018年5月10日',
        'is_activity_valid': True,
        'activity_rule': [
            '<span>1.</span>本活动面向返利投所有新老用户',
            '<span>2.</span>本活动共有劳、动、最、光、荣5张卡片，集齐5张卡片并合成为荣耀卡的用户将随机获得最低3元，最高188元现金红包；',
            '<span>3.</span>前50名首次合成卡片的用户额外获得100元京东卡，在活动结束后五个工作日内以短信形式发送到手机上；',
            '<span>4.</span>本活动于2018年5月11日10:00开奖，每位用户最多可合成3套荣耀卡，到时即可进行开奖，超出活动时间后卡片无法进行合成；',
            '<span>5.</span>活动期间，用户领取卡片的方式如下',
            '<span></span>（1）每日登录即可领取1张卡片；',
            '<span></span>（2）每日进行固收类产品投资后最多可领取1张，投资确认后增加领取次数；',
            '<span></span>（3）每日进行非固收类产品投资后最多可领取1张，投资确认后增加领取次数；',
            '<span></span>（4）每日分享本页面最多可领取1张；',
            '<span>6.</span>活动最终解释权归返利投所有，如有疑问请拨打客服电话<a href=" ">400-601-8132</a>'
        ],

        },
    'first_login_card_info': {
        'is_show': True,
        'title': '恭喜您, 获得一张劳动卡',
        'card_name': 'lao',
        },
    'cards_info': {
        'activity_title': '集荣耀,瓜分10万现金',
        'collect_card_reported': '100,000人已集齐, 5月11日10:00准时开奖', # 开奖后 '您已获得{获奖总金额}元现金{和100元京东卡}', # 未领奖 '荣耀已开奖，{集齐总人数}人瓜分10万现金'
        'collect_card_prize': '前50名首次合成卡片的用户额外获得100元京东卡',
        'composite_card_info': {    # 合卡信息
            'is_show': True,
            'button_name': '立即合成', # 再次合成
            'style': 'hecheng'
            },
        'my_cards_list': [
            {
                'name': 'lao',
                'is_show': True,
                'count': 2,
                'card_list': [1, 1]
            },
            {
                'name': 'dong',
                'is_show': True,
                'count': 2,
                'card_list': [1, 1]
            },
            {
                'name': 'zui',
                'is_show': True,
                'count': 2,
                'card_list': [1, 1]
            },
            {
                'name': 'guang',
                'is_show': False,
                'count': 0,
                'card_list': []
            },
            {
                'name': 'rong',
                'is_show': True,
                'count': 2,
                'card_list': [1, 1]
            },
            ],
        'rongyao': {
            'count': 1,
            'is_show': True,
            'card_list': [
                {
                    'type': 'weikaijiang',  # 'kaijiang', 'yikaijiang',
                    'card_name': 'rongyao',
                    'card_info': '5.11开奖',
                    'prize_content': [
                        '<span>88.88元</span>现金',
                        '<span>100元<>京东卡'
                    ],
                    'pc_prize_content': '<span>88.88<small>元</small></span>',
                },
            ]

            },
    'task_info': {
        'task_ntroduction': '每个任务完成后即可获取一次领卡机会（每日一次)',
        'task_list': [
            {
                'task_type': 'login',
                'task_name': '登录返利投',
                'task_button_name': '前往登录',
                'task_button_url': '/login',
                'action': 'draw_card', # 'link', 'share', 'not_click'
                'draw_count': 1,
            },
            {
                'task_type': 'fix',
                'task_name': '投资固收类产品',
                'task_button_name': '前往投资',
                'task_button_url': '/products',
                'action': 'link',
                'draw_count': 1,
            },
            {
                'task_type': 'other',
                'task_name': '投资非固收类产品',
                'task_button_name': '明日再来', # 前往投资
                'task_button_url': '/login', # 投资url, 抽卡api
                'action': 'not_click', #
                'draw_count': 1,
            },
            {
                'task_type': 'share',
                'task_name': '分享活动给好友',
                'task_button_name': '点击分享', # 明日再来
                'task_button_url': '/login',
                'action': 'share', # 'undefined'
                'draw_count': 1,
            },
        ]
        },
    'share_info': {
        "title": "集荣耀卡，分10万元！",
        "desc": "每人可合成3套卡片，瓜分更多红包大礼！",
        "url": "https://m.fanlitou.com/activity/",
        "img": "https://o0s106hgi.qnssl.com//group/icon/group_activity_icon.png",
    }

}
}

# 我的卡片页 /api/activity/my_cards/?user_name=''

data = {
    'success': True,
    'msg': '',
    'cards_info': {
        'activity_title': '集荣耀,瓜分10万现金',
        'collect_card_reported': '100,000人已集齐, 5月11日10:00准时开奖', # 开奖后 '您已获得{获奖总金额}元现金{和100元京东卡}', # 未领奖 '荣耀已开奖，{集齐总人数}人瓜分10万现金'
        'collect_card_prize': '前50名首次合成卡片的用户额外获得100元京东卡',
        'composite_card_info': {    # 合卡信息
            'is_show': True,
            'button_name': '立即合成', # 再次合成
            'style': 'hecheng'
        },
        'my_cards_list': [
            {
                'name': 'lao',
                'is_show': True,
                'count': 2,
                'card_list': [1, 1]
            },
            {
                'name': 'dong',
                'is_show': True,
                'count': 2,
                'card_list': [1, 1]
            },
            {
                'name': 'zui',
                'is_show': True,
                'count': 2,
                'card_list': [1, 1]
            },
            {
                'name': 'guang',
                'is_show': False,
                'count': 0,
                'card_list': []
            },
            {
                'name': 'rong',
                'is_show': True,
                'count': 2,
                'card_list': [1, 1]
            },
        ],
        'rongyao': {
            'count': 1,
            'is_show': True,
            'card_list': [
                {
                    'type': 'weikaijiang',  # 'kaijiang', 'yikaijiang',
                    'card_name': 'rongyao',
                    'card_info': '5.11开奖',
                    'prize_content': [
                        '<span>88.88元</span>现金',
                        '<span>100元<>京东卡'
                    ] ,
                    'pc_prize_content': '<span>88.88<small>元</small></span>',
                },
            ]

    },
        'share_info': {
            "title": "集荣耀卡，分10万元！",
            "desc": "每人可合成3套卡片，瓜分更多红包大礼！",
            "url": "https://m.fanlitou.com/activity/",
            "img": "https://o0s106hgi.qnssl.com//group/icon/group_activity_icon.png",
        }
    },
}



# 抽卡api /api/activity/draw_card/?user_name=''

data = {
    'success': True,
    'msg': '',
    'draw_card_info': {
        'title': '恭喜您获得一张劳动卡',
        'card_name': 'lao',
    }
}

# 合卡api /api/activity/composite_card/?user_name=''
data = {
    'success': True,
    'msg': '',
    'composite_share_info': {
        "title": "集荣耀卡，分10万元！",
        "desc": "我已集齐{集齐套数}套荣耀卡了，还不快来",
        "url": "https://m.fanlitou.com/activity/",
        "img": "https://o0s106hgi.qnssl.com//group/icon/group_activity_icon.png",
    },
}

# 领奖api /api/activity/draw_prize/?user_name=''
data = {
    'success': True,
    'msg': '',
    'prize_info': {
        'title': '恭喜您,获得88.88元现金',
        'red_packet_amount': '¥88.88',
        'red_packet_desc': '共3张荣耀卡',
    }
}
# print json.dumps(data, indent=2)


class WeightRandom(object):
    """
    带权重的随机抽奖
    """
    first_login_prob_map = {
        'lao': 30,
        'dong': 30,
        'zui': 20,
        'guang': 20
    }

    day_login_prod_map = {
        'lao': 35,
        'dong': 30,
        'zui': 15,
        'guang': 15,
        'rong': 5
    }

    fix_invest_prod_map = {
        'lao': 20,
        'dong': 20,
        'zui': 30,
        'guang': 20,
        'rong': 10
    }

    other_invest_prod_map = {
        'lao': 20,
        'dong': 20,
        'zui': 30,
        'guang': 20,
        'rong': 10
    }

    share_prod_map = {
        'lao': 35,
        'dong': 30,
        'zui': 15,
        'guang': 15,
        'rong': 5
    }
    prod_choice_map = {
        'first': first_login_prob_map,
        'login': day_login_prod_map,
        'fix': fix_invest_prod_map,
        'current': other_invest_prod_map,
        'share': share_prod_map
    }
    def __init__(self, task_name, term=1):
        self.dicts = self.prod_choice_map.get(task_name, '')
        self.term = term

    def choice(self):
        """
        抽奖
        :return >> prize: 'prize_name'
        """
        dicts = self.get_dicts_by_term()
        if not dicts:
            return None
        items = dicts.items()
        weight_list = [weight for _, weight in items]
        goods = [prize_name for prize_name, _ in items]
        weight_sum = sum(weight_list)
        acc_list = list(self.accumulate(weight_list))
        return goods[bisect.bisect_right(acc_list, random.uniform(0, weight_sum))]

    @staticmethod
    def accumulate(weight_list):
        """
        list累加
        :param weights: [10,40,50]
        :return: >> [10,50,100]
        """
        current = 0
        for weight in weight_list:
            current = current + weight
            yield current

    def get_dicts_by_term(self):
        """
        根据集卡套数,获取对应概率
        :return: >> new_dicts
        """
        dicts = self.dicts
        if not dicts:
            return None
        if not isinstance(self.term, int):
            self.term = int(self.term)
        if self.term > 1:
            power = float((self.term - 1) * 2)
            if 'guang' in dicts:
                dicts['guang'] = dicts['guang'] / power
                dicts['lao'] += dicts['guang'] * (power - 1)
            if 'rong' in dicts:
                dicts['rong'] = dicts['rong'] / power
                dicts['lao'] += dicts['rong'] * (power - 1)
        return dicts


@click.command()
@click.option('--times', default=1, type=click.IntRange(1, 5000), help='draw count')
@click.argument('type', type=click.STRING)
@click.argument('term', type=click.INT)
def draw_card(type, times, term):
    """
    抽奖
    :param type: 类型
    :param times: 几次
    :param term: 第几套
    :return:
    """
    import time
    t1 = time.clock()
    prize_list = []
    while len(prize_list)+1:
        if len(prize_list) < int(times):
            weight_obj = WeightRandom(type, term)
            prize_list.append(weight_obj.choice())
        else:
            break
    print prize_list
    t2 = time.clock()
    print t2 - t1

draw_card()
