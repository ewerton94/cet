from django.contrib import admin
from .models import Selecao,Candidato
from django.http import HttpResponse


def export_xls(modeladmin, request, querysete):
    import xlwt
    response = HttpResponse(content_type ='application/ms-excel')
    filename='inscritos_selecao.xls'
    response['Content-Disposition'] = 'attachment; filename=%s'%filename
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Inscritos')
    row_num = 0
    columns = [(candidato.nome, 10000) for candidato in Candidato.objects.all()]
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1
    col_num = 0
    row_num += 1
    aux=row_num
    from django.db import models
    for obj in Candidato.objects.all():
        col1 = [eval('obj.%s'%field.name) for field in Candidato._meta.fields if field.name!='data' and not isinstance(field,models.FileField)]
        for row_num in range(len(col1)):
            ws.write(row_num+aux, col_num, col1[row_num], font_style)
        col2 = [{'link':'http://pet.ufal.br'+str(eval('obj.%s.url'%field.name)),'name':str(field.name)} for field in Candidato._meta.fields if field.name!='data' and isinstance(field,models.FileField)]
        for row_num in range(len(col2)):
            ws.write(row_num+len(col1)+aux, col_num, xlwt.Formula('HYPERLINK("%s";"%s")' % (col2[row_num]['link'],col2[row_num]['name'])), font_style)
        col_num+=1
    wb.save(response)
    return response

export_xls.short_description = "Exportar para excel lista de inscritos"



class CandidatoAdmin(admin.ModelAdmin):
    model = Candidato
    list_display = ['nome','email']
    search_fields = ['nome']
    save_on_top = True
    actions=[export_xls,]
    
admin.site.register(Candidato,CandidatoAdmin)
admin.site.register(Selecao)


