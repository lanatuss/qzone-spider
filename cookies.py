# 登录后，将自己的 cookies 填写在这
cookies = {
    'pgv_pvi': '',
    'ptui_loginuin': '',
    'pt2gguin': '',
    'RK': '',
    'ptcz': '',
    'pgv_pvid': '',
    'tvfe_boss_uuid': '',
    'luin': '',
    'lskey': '',
    'QZ_FE_WEBP_SUPPORT': '',
    'cpu_performance_v8': '',
    'sd_userid': '',
    'sd_cookie_crttime': '',
    'o_cookie': '',
    'pac_uid': '',
    'pgv_si': '',
    'ptisp': '',
    'pgv_info': '',
    'uin': '',
    'skey': '',
    'p_uin': '',
    'pt4_token': '',
    'p_skey': '',
    'Loading': '',
    '__Q_w_s__QZN_TodoMsgCnt': '',
}


def getGTK(cookies):
    hashes = 5381
    for letter in cookies['p_skey']:
        hashes += (hashes << 5) + ord(letter)
    return hashes & 0x7fffffff


g_tk = getGTK(cookies)

if __name__ == '__main__':
    print(getGTK(cookies))
