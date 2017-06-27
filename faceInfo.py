# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: StudyTheCode
# author: "Lei Yong" 
# creation time: 2017/6/27 0027 16:13
# Email: leiyong711@163.com
import sys
import json
import urllib

reload(sys)
sys.setdefaultencoding('utf-8')

# 图片地址
imgurl = 'https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0=baike116,5,5,116,38/sign=72d2cfafbe3eb13550cabfe9c777c3b6/4610b912c8fcc3ce31252a749045d688d53f2094.jpg'


def Post():
    url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'  # 请求地址
    data = {'api_key': 'm_JZUUs-CzSzKsaqZa_TOAD7PMl4tv6r',
            'api_secret': 'SqeJQDQ_ZBpKKwxJUEgpq0fv-FY6OS6N',
            'image_url': imgurl,
            'return_attributes': 'gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity'}
    data = urllib.urlencode(data)
    return urllib.urlopen(url, data).read()

if __name__ == '__main__':
    html = Post()
    value = json.loads(html)
    try:
        face_roken = value['faces']
        attributes = face_roken[0]['attributes']
        print '性别分析结果：%s （Male:男，Female:女）' % attributes['gender']['value']
        print '年龄分析结果：%s' % attributes['age']['value']
        print '笑容分析结果：%s' % attributes['smile']['value']
        print '是否佩戴眼镜的分析结果：%s （None代表不佩戴眼镜，Dark代表佩戴墨镜，Normal代表佩戴普通眼镜）' \
              % attributes['glass']['value']
        print '人脸姿势分析结果：抬头 %s，旋转 %s，摇头 %s' \
              % (attributes['headpose']['pitch_angle'], attributes['headpose']['roll_angle'], attributes['headpose']['yaw_angle'])
        print '人种分析结果：%s （Asian代表亚洲人，White代表白人，Black代表黑人）' % attributes['ethnicity']['value']
    except:
        print '错误信息：%s'%face_roken["error_message"]
