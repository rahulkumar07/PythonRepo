import fitz
#run from ur Course directory
#Get start
for x in range(19):
    doc = fitz.open("Unit-"+str(x+1)+".pdf")
    print(doc)
    page = doc[1]
    print(page)
    text = "trade diversion"   #  'multilateral framework'
    text_instances = page.searchFor(text)
    for inst in text_instances:
        highlight = page.addHighlightAnnot(inst)
        print(inst)
    if(text_instances):
        doc.save("Unit-"+str(x+1)+"_output.pdf", garbage=4, deflate=True, clean=True)
