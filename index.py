from tkinter import *
import numpy as np
import pandas as pd
from PIL import ImageTk, Image  
import tkinter


symptoms=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']
# print(len(disease)) 41
remedy = [  # Fungal infection
    ['Tea tree oil', 'Garlic', 'Apple cider vinegar', 'Coconut oil'],
    # Allergy
    ['Honey', 'Turmeric', 'Aloe vera', 'Quercetin'],
    # GERD
    ['Baking soda', 'Ginger', 'Chamomile tea', 'Licorice root'],
    # Chronic cholestasis
    ['Turmeric', 'Indian gooseberry', 'Chicory', 'Dandelion'],
    # Drug Reaction
    ['Aloe vera', 'Oatmeal bath', 'Baking soda', 'Coconut oil'],
    # Peptic ulcer diseae
    ['Licorice root', 'Bananas', 'Cabbage juice', 'Garlic'],
    # AIDS
    ['Garlic', 'Echinacea', 'Mushrooms', 'Probiotics'],
    # Diabetes
    ['Cinnamon', 'Fenugreek', 'Gymnema', 'Bitter melon'],
    # Gastroenteritis
    ['Ginger', 'Peppermint oil', 'Chamomile tea', 'Apple cider vinegar'],
    # Bronchial Asthma
    ['Honey', 'Ginger', 'Garlic', 'Eucalyptus oil'],
    # Hypertension
    ['Garlic', 'Hawthorn', 'Fish oil', 'Beet juice'],
     # Migraine
    ['Ginger', 'Peppermint oil', 'Magnesium', 'Butterbur'],
    # Cervical spondylosis
    ['Turmeric', 'Ginger', 'Garlic', 'Epsom salt'],
    # Paralysis (brain hemorrhage)
    ['Ashwagandha', 'Ginkgo biloba', 'Ginger', 'Garlic'],
    # Jaundice
    ['Turmeric', 'Indian gooseberry', 'Papaya leaves', 'Lemon'],
    # Malaria
    ['Cinnamon', 'Ginger', 'Grapefruit seed extract', 'Artemisia annua'],
    # Chicken pox
    ['Oatmeal bath', 'Neem', 'Honey', 'Baking soda'],
    # Dengue
    ['Papaya leaf juice', 'Neem', 'Giloy', 'Fenugreek'],
    # Typhoid
    ['Garlic', 'Ginger', 'Honey', 'Bananas'],
    # Hepatitis A
    ['Milk thistle''Garlic', 'Turmeric'],
# Hepatitis B
['Milk thistle', 'Licorice root', 'Dandelion', 'Garlic'],
# Hepatitis C
['Milk thistle', 'Licorice root', 'Dandelion', 'Turmeric'],
# Hepatitis D
['Milk thistle', 'Licorice root', 'Dandelion', 'Garlic'],
# Hepatitis E
['Milk thistle', 'Licorice root', 'Dandelion', 'Turmeric'],
# Alcoholic hepatitis
['Milk thistle', 'Dandelion', 'Licorice root', 'Ginger'],
# Tuberculosis
['Garlic', 'Ginger', 'Turmeric', 'Eucalyptus oil'],
# Common Cold
['Honey', 'Ginger', 'Garlic', 'Echinacea'],
# Pneumonia
['Garlic', 'Ginger', 'Echinacea', 'Oregano oil'],
# Dimorphic hemmorhoids(piles)
['Witch hazel', 'Aloe vera', 'Epsom salt', 'Garlic'],
#heartattack
['Cayenne pepper', 'Garlic', 'Ginger', 'Hawthorn'],
# Varicoseveins
['Horse chestnut', 'Butchers broom', 'Grape seed extract', 'Witch hazel'],
# Hypothyroidism
['Ashwagandha', 'Selenium', 'Zinc', 'Coconut oil'],
# Hyperthyroidism
['Lemon balm', 'Bugleweed', 'Motherwort', 'Magnesium'],
# Hypoglycemia
['Cinnamon', 'Gymnema', 'Fenugreek', 'Chromium'],
# Osteoarthristis
['Turmeric', 'Ginger', 'Willow bark', 'Epsom salt'],
# Arthritis
['Turmeric', 'Ginger', 'Willow bark', 'Epsom salt'],
# (vertigo) Paroymsal Positional Vertigo
['Ginger', 'Coriander', 'Garlic', 'Vitamin D'],
# Acne
['Tea tree oil', 'Aloe vera', 'Green tea', 'Zinc'],
# Urinary tract infection
['Cranberry juice', 'D-mannose', 'Vitamin C', 'Garlic'],
# Psoriasis
['Aloe vera', 'Oatmeal bath', 'Turmeric', 'Vitamin D'],
# Impetigo
['Tea tree oil', 'Garlic', 'Manuka honey', 'Colloidal silver']

    ]

input_symptoms=[]
for x in range(0,len(symptoms)):
    input_symptoms.append(0)

# TESTING DATA df -------------------------------------------------------------------------------------
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

# print(df.head())

X= df[symptoms]

y = df[["prognosis"]]
np.ravel(y)
# print(y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[symptoms]
y_test = tr[["prognosis"]]
np.ravel(y_test)
# ------------------------------------------------------------------------------------------------------

def DecisionTree():

    from sklearn import tree

    DT_classification = tree.DecisionTreeClassifier()   # empty model of the decision tree
    DT_classification = DT_classification.fit(X,y)

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=DT_classification.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    ground_of_prediction = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(symptoms)):
        # print (k,)
        for z in ground_of_prediction:
            if(z==symptoms[k]):
                input_symptoms[k]=1

    inputtest = [input_symptoms]
    predict = DT_classification.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
        t4.delete("1.0", END)
        t4.insert(END, remedy[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")
        t4.delete("1.0", END)
        t4.insert(END, "Not Found")
        


def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    RT_classification = RandomForestClassifier()
    RT_classification = RT_classification.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=RT_classification.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    ground_of_prediction = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(symptoms)):
        for z in ground_of_prediction:
            if(z==symptoms[k]):
                input_symptoms[k]=1

    inputtest = [input_symptoms]
    predict = RT_classification.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[a])
        t5.delete("1.0", END)
        t5.insert(END, remedy[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")
        t5.delete("1.0", END)
        t5.insert(END, "Not Found")

def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    NB_classification = GaussianNB()
    NB_classification=NB_classification.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=NB_classification.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    ground_of_prediction = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for k in range(0,len(symptoms)):
        for z in ground_of_prediction:
            if(z==symptoms[k]):
                input_symptoms[k]=1

    inputtest = [input_symptoms]
    predict = NB_classification.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
        t6.delete("1.0", END)
        t6.insert(END, remedy[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")
        t6.delete("1.0", END)
        t6.insert(END, "Not Found")
# gui_stuff------------------------------------------------------------------------------------


root = tkinter.Tk()
root.configure(background='#86C8BC')

# entry variables
Symptom1 = StringVar()
Symptom1.set("Select Symptom")
Symptom2 = StringVar()
Symptom2.set("Select Symptom")
Symptom3 = StringVar()
Symptom3.set("Select Symptom")
Symptom4 = StringVar()
Symptom4.set("Select Symptom")
Symptom5 = StringVar()
Symptom5.set("Select Symptom")


# Heading
w2 = Label(root, justify=LEFT, text="sAnZeevni", fg="white", bg="#86C8BC")
w2.config(font=("MS Serif", 30))
w2.grid(row=1, column=1, columnspan=2, padx=50,pady=25)
w2 = Label(root, justify=LEFT, text="Calming Feels  When Nature Heels", fg="white", bg="#86C8BC")
w2.config(font=("Elephant", 16))
w2.grid(row=1, column=2, columnspan=2, padx=50,pady=25)



S1_labelLb = Label(root, text="Symptom 1", fg="white", bg="#86C8BC")
S1_labelLb.grid(row=9, column=0, pady=10, sticky=W)

S2_labelLb = Label(root, text="Symptom 2", fg="white", bg="#86C8BC")
S2_labelLb.grid(row=10, column=0, pady=10, sticky=W)

S3_labelLb = Label(root, text="Symptom 3", fg="white", bg="#86C8BC")
S3_labelLb.grid(row=11, column=0, pady=10, sticky=W)

S4_label = Label(root, text="Symptom 4", fg="white", bg="#86C8BC")
S4_label.grid(row=12, column=0, pady=10, sticky=W)

S5_label = Label(root, text="Symptom 5", fg="white", bg="#86C8BC")
S5_label.grid(row=13, column=0, pady=10, sticky=W)


R1 = Label(root, text="Remedy", fg="white", bg="#86C8BC")
R1.grid(row=15, column=2, pady=10,sticky=W)

R2 = Label(root, text="Remedy", fg="white", bg="#86C8BC")
R2.grid(row=17, column=2, pady=10, sticky=W)

R3 = Label(root, text="Remedy", fg="white", bg="#86C8BC")
R3.grid(row=19, column=2, pady=10, sticky=W)

# entries
OPTIONS = sorted(symptoms)


S1_label = OptionMenu(root, Symptom1,*OPTIONS)
S1_label.grid(row=9, column=1)

S2_label = OptionMenu(root, Symptom2,*OPTIONS)
S2_label.grid(row=10, column=1)

S3_label = OptionMenu(root, Symptom3,*OPTIONS)
S3_label.grid(row=11, column=1)

S4_label= OptionMenu(root, Symptom4,*OPTIONS)
S4_label.grid(row=12, column=1)

S5_label = OptionMenu(root, Symptom5,*OPTIONS)
S5_label.grid(row=13, column=1)


DT = Button(root, text="Possiblity1", command=DecisionTree,bg="green",fg="yellow")
DT.grid(row=15, column=0,padx=10)

RF = Button(root, text="Possiblity2", command=randomforest,bg="green",fg="yellow")
RF.grid(row=17, column=0,padx=10)

NB = Button(root, text="Possiblity3", command=NaiveBayes,bg="green",fg="yellow")
NB.grid(row=19, column=0,padx=10)

#textfileds
t1 = Text(root, height=1, width=40,bg="white",fg="black")
t1.grid(row=15, column=1, padx=10)

t2 = Text(root, height=1, width=40,bg="white",fg="black")
t2.grid(row=17, column=1 , padx=10)

t3 = Text(root, height=1, width=40,bg="white",fg="black")
t3.grid(row=19, column=1 , padx=10)

t4 = Text(root, height=1, width=40,bg="white",fg="black")
t4.grid(row=15, column=3, padx=10)

t5 = Text(root, height=1, width=40,bg="white",fg="black")
t5.grid(row=17, column=3 , padx=10)

t6 = Text(root, height=1, width=40,bg="white",fg="black")
t6.grid(row=19, column=3 , padx=10)
root.mainloop()