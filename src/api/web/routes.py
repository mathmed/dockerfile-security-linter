from .controllers.DockerfileAnalysis import DockerfileAnalysis

def routes(api):
    api.add_resource(DockerfileAnalysis, '/dockerfile-analysis')
