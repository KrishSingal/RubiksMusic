movesets = [
             ['L', "L'", 'L2', 'R', "R'", 'R2', 'U', "U'", 'U2', 'B', "B'", 'B2', 'D', "D'", 'D2', 'F', "F'", 'F2'],
             ['L', "L'", 'L2', 'R', "R'", 'R2', 'U', "U'", 'U2', 'D', "D'", 'D2', 'F2', 'B2'],
             ['U', "U'", 'U2', 'D', "D'", 'D2', 'L2', 'F2', 'R2', 'B2'],
             ['U2', 'L2', 'F2', 'R2', 'D2', 'B2']
           ]

masks = [{1: 'orange', 3: 'orange', 5: 'orange', 7: 'orange', 21: 'orange', 23: 'orange', 28: 'orange', 30: 'orange',
          32: 'orange', 34: 'orange', 48: 'orange', 50: 'orange'},

         {0: 'orange', 1: 'orange', 2: 'orange', 3: 'orange', 5: 'orange', 6: 'orange', 7: 'orange', 8: 'orange',
          27: 'orange', 28: 'orange', 29: 'orange', 30: 'orange', 32: 'orange', 33: 'orange', 34: 'orange',
          35: 'orange', 21: 'pink', 23: 'pink', 48: 'pink', 50: 'pink'},

         {0: 'original', 2: 'original', 6: 'original', 8: 'original', 9: 'original', 11: 'original', 15: 'original',
          17: 'original', 18: 'original', 20: 'original', 24: 'original', 26: 'original', 27: 'original',
          29: 'original', 33: 'original', 35: 'original', 36: 'original', 38: 'original', 42: 'original',
          44: 'original', 45: 'original', 47: 'original', 51: 'original', 53: 'original', 37: 'red', 39: 'red',
          41: 'red', 43: 'red', 19: 'original', 21: 'original', 23: 'original', 25: 'original', 10: 'original',
          12: 'original', 14: 'original', 16: 'original', 46: 'green', 48: 'green', 50: 'green', 52: 'green'},

         {0: 'original', 1: 'original', 2: 'original', 3: 'original', 4: 'original', 5: 'original', 6: 'original',
          7: 'original', 8: 'original', 9: 'original', 10: 'original', 11: 'original', 12: 'original', 13: 'original',
          14: 'original', 15: 'original', 16: 'original', 17: 'original', 18: 'original', 19: 'original',
          20: 'original', 21: 'original', 22: 'original', 23: 'original', 24: 'original', 25: 'original',
          26: 'original', 27: 'original', 28: 'original', 29: 'original', 30: 'original', 31: 'original',
          32: 'original', 33: 'original', 34: 'original', 35: 'original', 36: 'original', 37: 'original',
          38: 'original', 39: 'original', 40: 'original', 41: 'original', 42: 'original', 43: 'original',
          44: 'original', 45: 'original', 46: 'original', 47: 'original', 48: 'original', 49: 'original',
          50: 'original', 51: 'original', 52: 'original', 53: 'original'
          }
         ]

prune_depths = [10, 6, 5, 6]
