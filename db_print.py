import model
from sqlite3 import OperationalError


def _print():
    try:
        job_list = model.Model().fetch_all_data()
        title = ['name', 'url', 'last_build_number', 
                'last_successful_build_number', 'last_unsuccessful_build_number',
                'last_stable_build_number', 'health_color', 'health_description',
                'health_score', 'checked_at']

        if len(job_list):
            print("{:-<90}".format("-"))
            for row in job_list:
                index = 0
                for data in row:
                    print("{0:32}:  {1}".format(title[index], data))
                    index += 1
                print("{:-<90}".format("-"))

        else:
            print("No saved job yet")

    except OperationalError as err:
        print("\nError occurred: ", err)


if __name__ == '__main__':
   _print() 
