from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    DateField,
    TimeField,IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired

import pandas as pd

train_df = pd.read_csv('Data/train.csv')
val_df = pd.read_csv('Data/val.csv')
X_data = pd.concat([train_df,val_df],axis = 0).drop('price',axis=1)

class Inputform(FlaskForm):
    airline = SelectField(label='Airline',
                          choices=X_data.airline.unique().tolist(),
                          validators=[DataRequired()]
                          )
    source = SelectField(label='Source',
                         choices=X_data.source.unique().tolist(),
                         validators=[DataRequired()]
                         )
    destination = SelectField(label='Destination',
                         choices=X_data.destination.unique().tolist(),
                         validators=[DataRequired()]
                         )
    add_on = SelectField(label='add_on',
                         choices=X_data.additional_info.unique().tolist(),
                         validators=[DataRequired()]
                         )
    date_of_journey = DateField(label = 'Date of Journey',
                                validators=[DataRequired()]
                                )
    dep_time = TimeField(label = 'Departure Time',
                         validators=[DataRequired()]
                         )
    arrival_time = TimeField(label='Arrival Time',
                             validators=[DataRequired()]
                             )
    duration = IntegerField(label='Duration',
                            validators=[DataRequired()]
                            )
    total_stops = IntegerField(label='Total Stops',
                               validators=[DataRequired()]
                               )
    submit = SubmitField(label = 'predict')