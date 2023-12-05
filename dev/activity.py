
import pandas as pd
import random

class Activity:
    """
    A class representing educational activities for children.

    Parameters:
        x (int): The number of activities to generate.

    Attributes:
        x (int): The number of activities to generate.
        activities_list (list): A list of activity names.
        learning_goals (list): A list of corresponding learning goals for each activity.
        activity_ids (list): A list of unique activity IDs.
        activity_data (pd.DataFrame): A DataFrame containing activity details.

    Methods:
        generate_activity_ids(): Generates a list of unique activity IDs.
        generate_activity_data(): Generates activity data with shuffled IDs, activity names,
                                    and associated learning goals.
    """
    def __init__(self, x):
        self.x = x
        self.activities_list =  [
    "Alphabet Hopscotch",
    "Alphabet Scavenger Hunt",
    "Animal Sound Guessing Game",
    "Building Blocks Exploration",
    "Building Structures with Blocks",
    "Colour Mixing with Water Play",
    "Colourful Collage Art",
    "Colourful Sensory Bins",
    "Colourful Sorting Bins",
    "Counting and Sorting with Toys",
    "Counting with Counting Bears",
    "Finger Painting",
    "Group Building with Building Blocks",
    "Mirror Play for Self-Recognition",
    "Music and Movement",
    "Name Recognition with Name Tags",
    "Number Hunt in the Classroom",
    "Nursery Rhyme Sing-Along",
    "Outdoor Nature Exploration",
    "Outdoor Nature Hunt",
    "Outdoor Nature Scavenger Hunt",
    "Pattern Making with Blocks",
    "Play-dough Creations",
    "Play-dough Letter Creations",
    "Play-dough Shape Creations",
    "Puppet Show for Storytelling",
    "Puppet Theatre for Imagination",
    "Puzzles with Large Pieces",
    "Rhyming Words with Songs",
    "Sensory Play with Textures",
    "Shape Collages with Craft Materials",
    "Shape Hunt in the Classroom",
    "Shape Matching Game",
    "Shape Sorting with Blocks",
    "Sorting Colours with Household Items",
    "Sorting Objects by Size",
    "Story Sequencing with Pictures",
    "Story time with Picture Books",
    "Storytelling with Puppets",
    "Water Play with Floating Objects"
]
        self.learning_goals = [
    "Introduce basic counting skills",
    "Enhance problem-solving skills and hand-eye coordination",
    "Enhance fine motor skills and spatial awareness",
    "Enhance fine motor skills",
    "Reinforce colour recognition through everyday objects",
    "Develop language and sequencing skills through storytelling",
    "Explore primary colours and encourage experimentation",
    "Reinforce shape recognition and classification skills",
    "Develop size discrimination skills and enhance fine motor skills",
    "Foster curiosity about the environment and develop observation skills",
    "Introduce and reinforce basic patterning skills",
    "Introduce animal names and sounds",
    "Foster self-awareness",
    "Introduce basic shapes",
    "Introduce early numeracy skills through a fun scavenger hunt",
    "Reinforce shape recognition and creativity",
    "Introduce and reinforce basic counting and sorting skills",
    "Enhance language development and creativity through storytelling",
    "Encourage observation and appreciation of the environment",
    "Enhance fine motor skills and creativity through block building",
    "Reinforce letter recognition through an interactive scavenger hunt",
    "Develop hand-eye coordination",
    "Introduce letter recognition and gross motor skills",
    "Stimulate creativity and storytelling skills with puppet play",
    "Foster name recognition and social interaction",
    "Explore colours and develop fine motor skills through art",
    "Encourage creativity and fine motor skills",
    "Promote language development through storytelling",
    "Develop sensory awareness with different textures and colours",
    "Explore the environment and identify basic objects",
    "Promote teamwork, social skills, and creativity through block play",
    "Stimulate imagination and listening skills",
    "Reinforce shape recognition and encourage creativity",
    "Develop gross motor skills and rhythmic awareness",
    "Reinforce letter recognition and enhance fine motor skills",
    "Enhance language development through rhythm and melody",
    "Develop tactile awareness",
    "Introduce basic shapes",
    "Introduce basic colours and sorting skills",
    "Develop phonemic awareness through rhyming words and songs"
]
        self.activity_ids = self.generate_activity_ids()
        self.activity_data = self.generate_activity_data()

    def generate_activity_ids(self):
        return list(range(1, self.x+1))
        
    def generate_activity_data(self):
        random.shuffle(self.activity_ids)
        data = pd.DataFrame()
        data['activity_id'] = self.activity_ids
        data["activities"] = [self.activities_list[i] for i in range(self.x)]
        data['learning_goals'] = [self.learning_goals[i] for i in range(self.x)]

     
        return data
