def main(**kwargs):
    # pull extract status from xcom
    ti = kwargs["ti"]
    is_done = ti.xcom_pull(task_ids="extractUser", key="extract_user_done")
    is_done = is_done if is_done is not None else 0

    print(is_done, type(is_done))

    if is_done:
        return "done"
    else:
        return "transformUser"