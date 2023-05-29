from justpy import *


def Mysampleapp():


    def addnew(self,msg):
        counter.text = str(int(counter.text) + 1)


    def removedata(self,msg):
        counter.text = str(int(counter.text) - 1)
        



    # NOW CREATE QUASAR COMPONENT AND PAGE
    # NOW CREATE MODEL LIKE v-model in vue js
    app = QuasarPage(data={"name":"budi"})

    # NOW CREATE APP LAYOUT COLUMN
    layout = Div(classes="q-pa-md column",a=app)
    # AND a is YOU PARENT COMPONENT

    # NOW I CREATE 2 BUTTON COUNTER 
    myDIv = Div(classes="row q-pa-md q-ma-lg justify-between",
        a=layout
        )

    btnIncrement = QBtn(color="primary",
            icon="add",label="add",
            a=myDIv
            )
    counter = P(text="0",a=myDIv,style="font-size:50px")
    btnDecrement = QBtn(color="red",
            icon="remove",label="remove",
            a=myDIv
            )

    # NOW I CREATE BIND INPUT TEXT AND SEE YOU INPUT 

    secondDiv = Div(classes="row",a=layout)
    # YOU RESULT INPUT 
    resultText = H4(model=[app,"name"],a=layout)

    # AND NOW CREATE INPUT TEXT
    myinput = QInput(label="add new ",
        model=[app,"name"],a=layout
        )


    # NOW I CREATE CLICK EVENT
    btnIncrement.on("click",addnew)
    btnDecrement.on("click",removedata)
    return app




justpy(Mysampleapp)
# NOW RUN THIS APP
