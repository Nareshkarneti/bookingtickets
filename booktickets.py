import json
import string
import pandas as pd

class seat_arragements:
    def __init__(self,input_json, request_seats):
        f = open(input_json, )

        self.venue_available_seats = json.load(f)
        self.request_seats = request_seats
        self.arrangment_hash = []
        self.rows=self.venue_available_seats["venue"]["layout"]["rows"]
        self.columns =self.venue_available_seats["venue"]["layout"]["columns"]

    def available_seats(self):
        rows=self.venue_available_seats["venue"]["layout"]["rows"]
        columns =self.venue_available_seats["venue"]["layout"]["columns"]
        alphabet_array = list(string.ascii_lowercase)
        for i in range(rows):
            r_a = {}
            alph = alphabet_array[i]
            for c1 in range(columns):
                r_a[alph + str(c1 + 1)] = "A"
            print(r_a)
            self.arrangment_hash.append(r_a)
        return self.arrangment_hash

    def update_venue_seats_already_booked(self):
        occupied_seats=self.venue_available_seats['seats'].keys()
        if self.venue_available_seats['seats']:
            print("Blocking seats already in use")
            for seat in self.venue_available_seats['seats']:
                #print(seat)
                for i in range(len(occupied_seats)):
                    if self.arrangment_hash[i].get(seat)=='A':
                        self.arrangment_hash[i][seat]='U'

        #print(self.arrangment_hash)

    def find_best_seats(self):
        center_seat = int(self.columns / 2)
        print(center_seat)

        for arrangment in self.arrangment_hash:
           print(arrangment)
           row = list(arrangment.keys())[0]
           if self.request_seats>0:
               if  list(arrangment.values()).__contains__('U'):
                   print("row {} len {}".format(row,len(list(arrangment.values()))))
                   self.loop_through_center(arrangment,center_seat)
                   self.request_seats=self.request_seats - 1
           if self.request_seats==0:
               break;
        print("Final output ")
        print(self.arrangment_hash)
        return arrangment
    def loop_through_center(self,arrangment,center_seat):
        add = 0
        delete = 0
        row = list(arrangment.keys())[0]
        for l in range(self.request_seats):
            if l % 2 == 0:
                if arrangment[str(row[0])+str(center_seat + add)]== "A":
                    arrangment[str(row[0]) + str(center_seat + add)] = "U"
                    #print(arrangment)
                    add = add + 1
            else:
                delete = delete + 1
                if arrangment[str(row[0])+str(center_seat - delete)]== "A":
                    arrangment[str(row[0]) + str(center_seat - delete)] = "U"
                    #print(arrangment)
            self.request_seats =self.request_seats - 1



if __name__ == '__main__':
    ticket_1=seat_arragements("venune.json",3)
    print("preparing available seats")
    ticket_1.available_seats()
    print("updating seat for venue seats")
    ticket_1.update_venue_seats_already_booked()
    ticket_1.find_best_seats()
