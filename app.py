from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime
import yaml
from pytz import timezone
import pytz


## == Setup ====
app = Flask(__name__)
api = Api(app)

def load_configuration(file_path):
    """Load configuration from YAML file."""
    with open(file_path, 'r') as f:
        config = yaml.safe_load(f)
    return config


class JsonOut(Resource):
    """Generate simple json packet to display."""
    def get(self):
        config = load_configuration('config.yaml')
        strtz = config['flask']['tz']
        # Define the ZUL time
        zul_time = datetime.now(tz=pytz.utc)

        # Convert the ZUL time to Auckland Pacific time
        target_time = zul_time.astimezone(timezone(strtz))
        now_out = target_time.strftime("%Y-%m-%d %H:%M:%S")
        return {'timezone': strtz, 'time': now_out}


# == add the json out as a resource ==
api.add_resource(JsonOut, '/')

if __name__ == "__main__":
    
    config = load_configuration('config.yaml')
    flask_config = config['flask']
    flask_port = flask_config['port']
    flask_address = flask_config['ip_address']

    app.run(host=flask_address,port=flask_port, debug=True)

# == EoF ==