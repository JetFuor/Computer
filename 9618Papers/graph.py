graph = [["Shopping Centre", "Town Centre", 0.5], ["Town Centre", "Gardens", 1.5],
["Gardens", "Shopping Centre", 0.5], ["School", "Town Centre", 0.5],
["Town Centre", "River", 2.0], ["Town Centre", "Train Station", 2.5]
["Gardens", "River", 0.7], ["River", "Train Station", 1.2]
["School", "Train Station", 0.9]]


graph = {
    'shopping_center':{'town_center' : 0.5,'gardens' : 0.5},
    'town_center':{'shopping_center' : 0.5, 'school' : 0.5, 'river' : 2.0, 'gardens' : 1.5, 'train_station' : 2.5},
    'gardens':{'shopping_center' : 0.5, 'town_center' : 1.5, 'river' : 0.7},
    'school':{'town_center' : 0.5, 'train_station' : 0.9},
    'river':{'town_center' : 2.0, 'gardens' : 0.7, 'train_station' : 1.2},
    'train_station':{'school' : 0.9, 'town_center' : 2.5, 'river' : 1.2} 
}
# shopping to town
# shopping to garden
# twon to garden
# town to school
# town to river
# town to train

# garden to river
# river to train
# school to train