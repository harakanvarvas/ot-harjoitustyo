from invoke import task

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")
@task
def coverage_percent(ctx):
    ctx.run("coverage report -m")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def start(ctx):
    ctx.run("")
