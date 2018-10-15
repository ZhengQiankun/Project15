from flask import current_app
from flask import request, jsonify,make_response

from info import constants
from info import redis_store
from info.modules.passport import passport_blue
from info.utils.captcha.captcha import captcha

#获取返回,一张图片
# 请求路径: /passport/image_code
# 请求方式: GET
# 请求参数: cur_id, pre_id
# 返回值: 图片验证码
from info.utils.response_code import RET


@passport_blue.route('/image_code')
def image_code():
    """
    思路分析:
    1.获取参数
    2.校验参数(为空校验)
    3.生成图片验证码
    4.保存图片验证码到redis
    5.判断是否有上个图片验证码编号,有则删除
    6.返回图片验证码即可
    :return:
    """


    # 1.获取参数
    cur_id = request.args.get("cur_id")
    pre_id = request.args.get("pre_id")

    # 2.校验参数(为空校验)
    if not cur_id:
        return jsonify(errno=RET.PARAMERR,errmsg="图片验证码编号不存在")

    # 3.生成图片验证码
    name, text, image_data = captcha.generate_captcha()

    try:
        # 4.保存图片验证码到redis
        redis_store.set("image_code:%s"%cur_id,text,constants.IMAGE_CODE_REDIS_EXPIRES)

        # 5.判断是否有上个图片验证码编号,有则删除
        if pre_id:
            redis_store.delete("image_code:%s"%pre_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg="图片验证码操作异常")

    # 6.返回图片验证码即可
    response = make_response(image_data)
    response.headers["Content-Type"] = "image/jpg"
    return response


