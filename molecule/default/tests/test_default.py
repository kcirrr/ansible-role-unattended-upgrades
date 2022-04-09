"""Role testing files using testinfra."""


def test_packages(host):
    pkg = host.package("unattended-upgrades")
    assert pkg.is_installed


def test_unattended_upgrades_file(host):
    f = host.file("/etc/apt/apt.conf.d/50unattended-upgrades")
    assert f.exists
    assert f.contains("Unattended-Upgrade::Mail")
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644


def test_unattended_upgrades_override_file(host):
    f = host.file("/etc/systemd/system/apt-daily-upgrade.timer.d/override.conf")  # noqa: E501
    assert f.exists
    assert f.contains("OnCalendar")
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644


def test_unattended_upgrades_enabled(host):
    s = host.service("apt-daily-upgrade.timer")
    assert s.is_running
    assert s.is_enabled
