import telebot,json,os
token="#token"
bot=telebot.TeleBot(str(token))
@bot.message_handler(content_types=["document"])
def h(m):
    file=bot.get_file(m.document.file_id)
    fo=bot.download_file(file.file_path)
    with open(m.document.file_name,"wb") as f:
        fop=f.write(fo)
        f.close()
    with open(m.document.file_name,"rb") as d:
        if m.caption==None:
            bot.send_document(m.chat.id,d)
        else:
            bot.send_document(m.chat.id,d,caption=m.caption)
        os.remove(m.document.file_name)
@bot.message_handler(content_types=["photo"])
def ph(me):
    photoo=bot.get_file(str(str(me.photo[3]).split("'file_id': '")[1]).replace("'}",""))
    dophoto=bot.download_file(photoo.file_path)
    with open("photo.png","wb") as pho:
        wp=pho.write(dophoto)
    with open("photo.png","rb") as opho:
        if me.caption==None:
            bot.send_photo(me.chat.id,opho)
        else:
            bot.send_photo(me.chat.id,opho,caption=str(me.caption))
        os.remove("photo.png")
@bot.message_handler(content_types=["video"])
def video(mess):
    makeid_json=json.dumps(mess.video.file_id)
    video_get=bot.get_file(str(makeid_json).replace('"',""))
    down_video=bot.download_file(video_get.file_path)
    print(mess)
    with open("video.mp4","wb") as ci:
        wp=ci.write(down_video)
    with open("video.mp4","rb") as l:
        if mess.caption==None:
            bot.send_video(mess.chat.id,l)
        else:
            bot.send_video(mess.chat.id,l,caption=str(mess.caption))
        os.remove("video.mp4")
@bot.message_handler(content_types=["text"])
def tect(messa):
    if messa.text=="/start":
        bot.send_message(messa.chat.id,f"welcome {messa.chat.first_name} send any content to resend it \ncopyright: @Kaero7 ")
    else:
        bot.send_message(messa.chat.id,str(messa.text))
@bot.message_handler(content_types=["sticker"])
def stk(messk):
    file_ids=messk.sticker.file_id
    sticker_get=bot.get_file(file_ids)
    download_sticker=bot.download_file(sticker_get.file_path)
    print(messk)
    with open("sticker.webp","wb") as stu:
        stki=stu.write(download_sticker)
    with open("sticker.webp","rb") as rbstick:
        bot.send_sticker(messk.chat.id,rbstick)
        os.remove("sticker.webp")
@bot.message_handler(content_types=["animation"])
def skskks(op):
    get_animation=bot.get_file(op.animation.file_id)
    download_animation=bot.download_file(get_animation.file_path)
    with open("ani.mp4","wb") as wa:
        wa.write(download_animation)
    with open("ani.mp4","rb") as ra:
        if op.caption== None:
            bot.send_animation(op.chat.id,ra)
        else:
            bot.send_animation(op.chat.id,ra,caption=op.caption)
        os.remove("ani.mp4")
@bot.message_handler(content_types=["contact"])
def con(cont):
    bot.send_contact(cont.chat.id,cont.contact.phone_number,cont.contact.first_name)
@bot.message_handler(content_types=["voice"])
def xo(voinfo):
    get_voice=bot.get_file(voinfo.voice.file_id)
    download_voice=bot.download_file(get_voice.file_path)
    
    with open("voice.oga","wb") as wbv:
        wbv.write(download_voice)
    with open("voice.oga","rb") as rbv:
        bot.send_voice(voinfo.chat.id,rbv,caption=voinfo.caption)
        os.remove("voice.oga")
@bot.message_handler(content_types=["location"])
def locat(loinf):
    bot.send_location(loinf.chat.id,loinf.location.latitude,loinf.location.longitude)
@bot.message_handler(content_types=["audio"])
def audi(meau):
    get_audio=bot.get_file(meau.audio.file_id)
    download_audio=bot.download_file(get_audio.file_path)
    namef=str(str(meau).split("'file_name': '")[1]).split("',")[0]
    with open(namef,"wb") as wbaud:
        wbaud.write(download_audio)
    with open(namef,"rb") as rbaud:
        if meau.caption==None:
            bot.send_audio(meau.chat.id,rbaud)
        else:
            bot.send_audio(meau.chat.id,rbaud,caption=meau.caption)
        os.remove(namef)
bot.polling()


