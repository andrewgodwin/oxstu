news        = Section(title='news', order=0)
debate      = Section(title='debate', order=1)
features    = Section(title='features', order=2)
arts        = Section(title='arts', order=3, parent=arts)
theatre     = Section(title='theatre', order=5, parent=arts)
film        = Section(title='film', order=6, parent=arts)
music       = Section(title='music', order=7, parent=arts)
fashion     = Section(title='fashion', order=8)
sport       = Section(title='sport', order=4)

section_list = [
        news,
        debate,
        features,
        arts,
        theatre,
        film,
        music,
        fashion,
        sport,
        ]

for sec in section_list: sec.save()
