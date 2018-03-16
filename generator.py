from pdb import set_trace
from subprocess import call
from create_project.main import make_new_project
from code_push.main import integrate_code_push
from web_deploy.main import integrate_web_deploy
from fastlane.main import integrate_fastlane
from circle_ci.main import integrate_circle_ci

make_new_project()
integrate_code_push()
integrate_web_deploy()
integrate_fastlane()
integrate_circle_ci()