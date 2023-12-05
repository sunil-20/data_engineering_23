# assessment.py
import pandas as pd
import random

class Assessment:
    """
    A class representing kids assessments with associated details.

    Parameters:
    - x (int): The number of assessments to generate.
    - uid_gen (object): An instance of a UID generator for creating unique IDs.
    - kid_instance (object): An instance of the Kid class to fetch kid IDs.
    - activity_instance (object): An instance of the Activity class to fetch activity IDs.

    Attributes:
    - x (int): The number of assessments to generate.
    - uid_gen (object): An instance of a UID generator for creating unique IDs.
    - kid_instance (object): An instance of the Kid class to fetch kid IDs.
    - activity_instance (object): An instance of the Activity class to fetch activity IDs.
    - behavior (list): A list of possible behaviors for assessments.
    - parent_advice (list): A list of advice for parents based on assessment results.
    - assessment_data (DataFrame): A pandas DataFrame containing information about the generated assessments.

    Methods:
    - generate_assessment_data(): Generates a pandas DataFrame with details of the assessments, including ID, kid ID, activity ID, assessment code, behavior, and advice for parents.

    Usage:
    assessment_instance = Assessment(x=10, uid_gen=my_uid_generator, kid_instance=my_kids, activity_instance=my_activities)
    generated_assessment_data = assessment_instance.assessment_data
    """
    counter = 1
    def __init__(self, x, uid_gen, kid_instance, activity_instance):
        self.x = x
        self.uid_gen = uid_gen
        # kid ids
        self.kid_instance = kid_instance
        # activity ids
        self.activity_instance = activity_instance
        
        self.behavior = [
    "Excessive Shyness or Withdrawal",
    "Persistent Disinterest in Activities",
    "Extreme Hyperactivity",
    "Persistent Trouble Making Friends",
    "Frequent Physical Ailments",
    "Extreme Aggressiveness Towards Peers",
    "Excessive Withdrawal from Classroom Activities",
    "Consistent and Intense Tantrums",
    "Difficulty in Engaging with Others",
    "Persistent Inability to Follow Simple Instructions",
    "Extreme Hyperactivity Beyond Typical Toddler Energy",
    "Regression in Language Skills",
    "Persistent Inattention during Classroom Activities",
    "Unusual Fixation on Certain Objects or Topics",
    "Frequent Physical Complaints Without Apparent Cause",
    "Extreme Difficulty in Sharing or Taking Turns",
    "Consistent Isolation from Peers",
    "Frequent and Intense Tantrums Beyond Age Norms",
    "Difficulty in Following Simple Instructions",
    "Excessive Resistance to Routine Changes",
    "Persistent Lack of Interest in Classroom Activities",
    "Regression in Language or Communication Skills",
    "Extreme Difficulty in Managing Frustration"
]
        self.parent_advice = [
    "If the child consistently isolates themselves from peers, encourage social interactions at home and consult with a paediatrician to ensure there are no emotional or developmental concerns.",
    "If the child consistently displays extreme aggression towards peers, encourage positive play at home and consult with a paediatrician to rule out any underlying behavioural or emotional issues.",
    "If the child consistently struggles to engage with peers or teachers, encourage social interactions at home and consider consulting with a paediatrician to assess social development.",
    "If the child consistently withdraws from classroom activities, create a supportive environment at home and encourage participation in various activities. Consult with a paediatrician to ensure there are no developmental concerns.",
    "If the child displays excessive hyperactivity, ensure a balance of physical activities and routines at home. Consult with a paediatrician to assess whether there may be attention or hyperactivity concerns.",
    "If the child displays intense fixation, encourage a variety of interests at home. Consult with a paediatrician to rule out any obsessive behaviours or developmental concerns.",
    "If the child frequently complains of physical ailments without apparent cause, consult with a paediatrician to rule out any underlying health concerns and ensure the child's overall well-being.",
    "If the child frequently struggles with sharing or taking turns, practice these skills at home and consider consulting with a paediatrician to assess social development.",
    "If the child has consistent difficulty following basic instructions, practice clear communication at home. If issues persist, consult with a paediatrician to rule out any developmental or cognitive concerns.",
    "If the child regresses in language skills, engage in consistent communication at home and consult with a paediatrician to rule out any speech or language developmental concerns.",
    "If the child struggles significantly with sharing or taking turns, practice these skills at home and consider consulting with a paediatrician to assess social development.",
    "If the child struggles to make friends, work on social skills at home and encourage positive interactions. Consult with a paediatrician to rule out any underlying social or developmental challenges.",
    "If the child struggles to focus during classroom activities, create a calm and organized study environment at home. Consult with a paediatrician to explore attention-related concerns.",
    "While tantrums are common, persistent and intense outbursts may signal underlying issues. Establish clear boundaries at home and consult with a paediatrician to explore potential triggers or behavioural concerns.",
    "If the child consistently shows disinterest in activities they once enjoyed, explore new activities at home and discuss any concerns with a paediatrician to rule out emotional or developmental issues.",
    "If the child consistently withdraws or is excessively shy in class, try to create a supportive environment at home. Encourage social interactions through play-dates and consult with a paediatrician to ensure there are no developmental concerns.",
    "No abnormal behaviour"
]

        self.assessment_data = self.generate_assessment_data()

    def generate_assessment_data(self):
        data = pd.DataFrame()
        
        kid_ids = self.kid_instance.kid_ids
        print(type(kid_ids))
        random.shuffle(kid_ids)
        activity_ids = self.activity_instance.activity_ids
     
        for i in range (self.x):
            data.loc[i, "assessment_id"] = self.counter
            self.counter +=1
            data.loc[i, "kid_id"] = kid_ids[i]
            data.loc[i, "activity_id"] = random.choice(activity_ids)

            data.loc[i, "assessment_code"] = self.uid_gen.f.random_element([25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

            data.loc[i, "behaviour"] = self.uid_gen.f.random_element(elements = self.behavior)

            data.loc[i, "advice_parents"] = self.uid_gen.f.random_element(elements = self.parent_advice)

        return data