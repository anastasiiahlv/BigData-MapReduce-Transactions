import subprocess
import sys

HADOOP = "/opt/hadoop-3.2.1/bin/hadoop"
HDFS = "/opt/hadoop-3.2.1/bin/hdfs"

HDFS_INPUT = "/transactions/input/transactions.csv"
HDFS_JOB1 = "/transactions/output/job1"
HDFS_JOB2 = "/transactions/output/job2"

STREAMING_JAR = (
    "/opt/hadoop-3.2.1/share/hadoop/tools/lib/"
    "hadoop-streaming-3.2.1.jar"
)

BASE = "/workspace/src"


def run_command(command):
    print("\nRunning: {}".format(" ".join(command)))
    subprocess.run(command, check=True)


def remove_hdfs_path(path):
    subprocess.run(
        [HDFS, "dfs", "-rm", "-r", "-f", path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False
    )


def run_job1():
    remove_hdfs_path(HDFS_JOB1)

    run_command([
        HADOOP, "jar", STREAMING_JAR,
        "-D", "mapreduce.job.reduces=2",
        "-files",
        "{}/job1_mapper.py,{}/job1_reducer.py".format(BASE, BASE),
        "-mapper", "python3 job1_mapper.py",
        "-reducer", "python3 job1_reducer.py",
        "-input", HDFS_INPUT,
        "-output", HDFS_JOB1
    ])


def run_job2():
    remove_hdfs_path(HDFS_JOB2)

    run_command([
        HADOOP, "jar", STREAMING_JAR,
        "-D", "mapreduce.job.reduces=1",
        "-files",
        "{}/job2_mapper.py,{}/job2_reducer.py".format(BASE, BASE),
        "-mapper", "python3 job2_mapper.py",
        "-reducer", "python3 job2_reducer.py",
        "-input", HDFS_JOB1,
        "-output", HDFS_JOB2
    ])


def main():
    try:
        run_job1()
        print("\nJob 1 successfully completed.")

        run_job2()
        print("\nJob 2 successfully completed.")

        print("\nFinal result:")
        subprocess.run(
            [HDFS, "dfs", "-cat", HDFS_JOB2 + "/part-*"],
            check=True
        )

    except subprocess.CalledProcessError as error:
        print("Error Hadoop: {}".format(error),
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
