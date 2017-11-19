import sqlite3
import jenkinsapp 

class Model:
    def __init__(self):

        self.job_list = jenkinsapp.get_jobs_info()

        self.db = sqlite3.connect('mydb')

    def create_table(self):
        cursor = self.db.cursor()

        cursor.execute(
            '''
                CREATE TABLE IF NOT EXISTS 
                jobs(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        url TEXT,
                        last_build_number TEXT,
                        last_successful_build_number TEXT,
                        last_unsuccessful_build_number TEXT,
                        last_stable_build_number TEXT,
                        health_color TEXT,
                        health_description TEXT,
                        health_score TEXT
                    )
            '''
        )

        self.db.commit()

    def insert_data(self):

        if len(self.job_list):

            self.create_table()

            cursor = self.db.cursor()
            cursor.executemany(
                '''
                    INSERT INTO 
                    jobs (
                            name,
                            url,
                            last_build_number,
                            last_successful_build_number,
                            last_unsuccessful_build_number,
                            last_stable_build_number,
                            health_color,
                            health_description,
                            health_score
                    )
                    VALUES(?,?,?,?,?,?,?,?,?)
                ''',
                self.job_list
            )

            self.db.commit()
            self.db.close()
            print("Data successfully inserted!")

        else:
            print('No job yet')

    def fetch_all_data(self):

        cursor = self.db.cursor()
        cursor.execute(
            '''
                SELECT 
                    name,
                    url,
                    last_build_number,
                    last_successful_build_number,
                    last_unsuccessful_build_number,
                    last_stable_build_number,
                    health_color,
                    health_description,
                    health_score
                FROM
                    jobs
            '''
        )

        for row in cursor:
            print(row)
            print()

        self.db.close()


if __name__ == '__main__':
    model = Model()
    model.insert_data()
