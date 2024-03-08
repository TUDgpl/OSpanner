import subprocess
import glob
import tempfile
solver_path = "D:\\GIT\\OriSpanner\\build\\src\\Debug\\OriSpanner.exe"
instances_path = "D:/GIT/OriSpannerP/instances/1D/Uniform/*.txt"
def run_solver(tempf, file_name):
    comd = solver_path + " "
    proc = subprocess.Popen([comd, "-f", file_name], stdout=tempf)
    proc.wait()
    tempf.seek(0)
    return tempf.read()

    #comd += file_name
    #subprocess.call([comd, "-f", file_name])
def get_ori(output):
    o = str(output).split(" ")
    print(o)
    return float(o[-1].replace('\'', ''))

def run_experiments():
    solutions = {}
    for f in glob.glob(instances_path, recursive=True):
        with tempfile.TemporaryFile() as tempf:
            print(f)
            output = run_solver(tempf, f)
            print(f)
            solutions[f[f.rindex('\\')+1:]] = get_ori(output)
    return solutions

solutions = {}
if __name__ == "__main__":
    for f in glob.glob(instances_path, recursive=True):
        with tempfile.TemporaryFile() as tempf:
            print(f)
            output = run_solver(tempf, f)
            print(f)
            solutions[f[f.rindex('\\')+1:]] = get_ori(output)
    print(solutions)


