import ephem

# Enter start_date and end_date as strings with '/' seperators, i.e., '2017/8/3'.
# fm_series('1985/7/1', '2000/1/1')
# Returns a list of full moon dates in the format of 'Thu, Jan 20 19:40:27 2000'. 
# Returns 'Sat May 29 22:39:52 1999 Blue Moon' on a second full moon in a single month.

def fm_series(start_date, end_date):
    lst = []
    start_date = ephem.date(start_date)
    end_date = ephem.date(end_date)
    nfm_sdt = ephem.next_full_moon(start_date)
    nfm_ct = ephem.localtime(nfm_sdt).ctime()
    lst.append(nfm_ct)
    while start_date < end_date:
        start_date = ephem.date(nfm_sdt + 1)
        nfm_sdt = ephem.next_full_moon(start_date)
        if (nfm_sdt.tuple()[1] == start_date.tuple()[1]):          
                nfm_ct_1 = str(ephem.localtime(nfm_sdt).ctime()) + "  -- Blue Moon "
                nfm_sdt = ephem.next_full_moon(nfm_sdt + 1)
                nfm_ct = ephem.localtime(nfm_sdt).ctime()
                lst.append(nfm_ct_1)
                lst.append(nfm_ct)
        else:
            nfm_ct = ephem.localtime(nfm_sdt).ctime()
            lst.append(nfm_ct)

    # print(lst)
    return lst

# fm_series('1985/7/1', '1985/9/1')
# # fm_series('2017/2/20', '2058/2/16')
# # # 2058,2,16
# print("Test")

def flmoons_since(start_date, end_date):
    lst = []
    fm_ct = 1
    bm_ct = 0
    start_date = ephem.date(start_date)
    end_date = ephem.date(end_date)
    nfm_stdt = ephem.next_full_moon(start_date)
    fm_ct += 1
    while start_date < end_date:
        start_date = ephem.date(nfm_stdt + 1)
        nfm_stdt = ephem.next_full_moon(start_date)
        if (nfm_stdt.tuple()[1] == start_date.tuple()[1]):
            nfm_stdt = ephem.next_full_moon(nfm_stdt + 1)
            fm_ct += 1
            bm_ct += 1
        else:
            fm_ct += 1
    # print("Full moon count =: " + str(fm_ct))
    # print("Blue moon count =: " + str(bm_ct))
    return ([fm_ct, bm_ct])

# flmoons_since('1985/7/1', '1995/9/1')


    

# d = ephem.date('1985/7/30')
# dt = ephem.next_full_moon(d)
# fmd_lt = ephem.localtime(dt).ctime()
# print("Next full moon: " + fmd_lt)
# d2 = ephem.date(dt)
# d2t_nfm = ephem.next_full_moon(d2)
# fm_d2_dt = ephem.localtime(d2t_nfm)
# fm_d2 = ephem.localtime(d2t_nfm).ctime()
# print(fm_d2)
# nw = ephem.now()
# print(nw)
# print( d2 < nw)
# print(fm_d2 + " Moon")
# print("Next_full_moon:")
# print(d2t_nfm)
# print("******")
# d2t_pfm = ephem.previous_full_moon(d2)
# print(d2t_pfm)
# print("*******")

# a = ephem.date('2016/1/1')
# b = ephem.date('2017/1/1')
# print(a)
# print(b)
# print(b - a)
