from dianping_comment import DianpingComment

COOKIES = 'pgv_pvid=7653737920;uin=o0375860950; RK=/V41iGnGTc; ptcz=b3a338b9d5eff5b2f67a68ae4985c85d35aafbb287322e2205ecd45a93dbedfe;o_cookie=375860950; pac_uid=1_375860950;pgv_info=ssid=s7674872102&pgvReferrer=; skey=@AFOYSALy3; qm_authimgs_id=2; qm_verifyimagesession=h01535fb3ef1f56e570e2dd69a1763a8b5969c70c90efabb901d0d5c13728eabe0f732bb3350905ded8; iip=0; mpuv=da2df76f-14fa-42b0-36b7-2fe652ac4d29'


class Customer(DianpingComment):

    def _data_pipeline(self, data):
        print(data)


if __name__ == "__main__":
    dianping = Customer('3262456', cookies=COOKIES)
    dianping.run()
