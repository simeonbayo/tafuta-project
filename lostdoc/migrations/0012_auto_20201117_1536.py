# Generated by Django 3.1.1 on 2020-11-17 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostdoc', '0011_auto_20201028_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='district',
            field=models.CharField(choices=[('Buikwe', 'Buikwe'), ('Bukomansimbi', 'Bukomansimbi'), ('Butambala', 'Butambala'), ('Buvuma', 'Buvuma'), ('Gomba', 'Gomba'), ('Kalangala', 'Kalangala'), ('Kalungu', 'Kalungu'), ('Kampala', 'Kampala'), ('Kayunga', 'Kayunga'), ('Kiboga', 'Kiboga'), ('Kyankwanzi', 'Kyankwanzi'), ('Luweero', 'Luweero'), ('Lwengo', 'Lwengo'), ('Lyantonde', 'Lyantonde'), ('Masaka', 'Masaka'), ('Mityana', 'Mityana'), ('Mpigi', 'Mpigi'), ('Mubende', 'Mubende'), ('Mukono', 'Mukono'), ('Nakaseke', 'Nakaseke'), ('Nakasongola', 'Nakasongola'), ('Rakai', 'Rakai'), ('Sembabule', 'Sembabule'), ('Wakiso', 'Wakiso'), ('Amuria', 'Amuria'), ('Budaka', 'Budaka'), ('Bududa', 'Bududa'), ('Bugiri', 'Bugiri'), ('Bukedea', 'Bukedea'), ('Bukwa', 'Bukwa'), ('Bulambuli', 'Bulambuli'), ('Busia', 'Busia'), ('Butaleja', 'Butaleja'), ('Buyende', 'Buyende'), ('Iganga', 'Iganga'), ('Jinja', 'Jinja'), ('Kaberamaido', 'Kaberamaido'), ('Kaliro', 'Kaliro'), ('Kamuli', 'Kamuli'), ('Kapchorwa', 'Kapchorwa'), ('Katakwi', 'Katakwi'), ('Kibuku', 'Kibuku'), ('Kumi', 'Kumi'), ('Kween', 'Kween'), ('Luuka', 'Luuka'), ('Manafwa', 'Manafwa'), ('Mayuge', 'Mayuge'), ('Mbale', 'Mbale'), ('Namayingo', 'Namayingo'), ('Namutumba', 'Namutumba'), ('Ngora', 'Ngora'), ('Pallisa', 'Serere'), ('ironko', 'ironko'), ('Soroti', 'Soroti'), ('Tororo', 'Tororo'), ('Abim', 'Abim'), ('Adjumani', 'Adjumani'), ('Agago', 'Agago'), ('Alebtong', 'Alebtong'), ('Amolatar', 'Amolatar'), ('Amudat', 'Amudat'), ('Amuru', 'Amuru'), ('Apac', 'Apac'), ('Arua', 'Arua'), ('Dokolo', 'Dokolo'), ('Gulu', 'Gulu'), ('Kaabong', 'Kaabong'), ('Kitgum', 'Kitgum'), ('Koboko', 'Koboko'), ('Kole', 'Kole'), ('Kotido', 'Kotido'), ('Lamwo', 'Lamwo'), ('Lira', 'Lira'), ('Maracha', 'Maracha'), ('Moroto', 'Moroto'), ('Moyo', 'Moyo'), ('Nakapiripirit', 'Nakapiripirit'), ('Napak', 'Napak'), ('Nebbi', 'Nebbi'), ('Nwoya', 'Nwoya'), ('Otuke', 'Otuke'), ('Oyam', 'Oyam'), ('Pader', 'Pader'), ('Yumbe', 'Yumbe'), ('Zombo', 'Buhweju'), ('Buliisa', 'Bundibugyo'), ('Bushenyi', 'Bushenyi'), ('Hoima', 'Hoima'), ('Ibanda', 'Ibanda'), ('Isingiro', 'Isingiro'), ('Kabale', 'Kabale'), ('Kabarole', 'Kabarole'), ('Kamwenge', 'Kamwenge'), ('Kanungu', 'Kanungu\t'), ('Kasese', 'Kasese'), ('Kibaale', 'Kibaale\t'), ('Kiruhura', 'Kiruhura'), ('Kiryandongo', 'Kiryandongo'), ('Kisoro', 'Kisoro'), ('Kyegegwa', 'Kyegegwa'), ('Kyenjojo', 'Kyenjojo'), ('Masindi', 'Masindi'), ('Mbarara', 'Mbarara'), ('Mitooma', 'Mitooma'), ('Ntoroko', 'Ntoroko'), ('Ntungamo', 'Ntungamo'), ('Rubirizi', 'Rubirizi'), ('Rukungiri', 'Rukungiri'), ('Sheema', 'Sheema'), ('Kagadi', 'Kagadi'), ('Kakumiro', 'Kakumiro'), ('Omoro', 'Omoro'), ('Rubanda', 'Rubanda'), ('Namisindwa', 'Namisindwa'), ('Pakwach', 'Pakwach'), ('Butebo', 'Butebo'), ('Rukiga', 'Rukiga'), ('Kyotera', 'Kyotera'), ('Bunyangabu', 'Bunyangabu'), ('Nabilatuk', 'Nabilatuk'), ('Bugweri', 'Bugweri'), ('Kasanda', 'Kasanda\t'), ('Kwania', 'Kwania'), ('Kapelebyong', 'Kapelebyong'), ('Kibuube', 'Kibuube'), ('Obongi', 'Obongi'), ('Kazo', 'Kazo'), ('Rwampara', 'Rwampara'), ('Kitagwenda', 'Kitagwenda'), ('Madi-Okollo', 'Madi-Okollo'), ('Karenga', 'Karenga'), ('Lusot', 'Lusot')], default='Kampala', max_length=50),
        ),
    ]
