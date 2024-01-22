%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     zenergy
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Exposes the energy counters that are reported via the Running Average Power Limit (RAPL) Model-specific Registers (MSRs) via the hardware monitor (HWMON) sysfs interface.
License:  GPLv2
URL:      https://github.com/BoukeHaarsma23/zenergy

Source:   %{url}/archive/refs/heads/master.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Based on AMD_ENERGY driver, but with some jiffies added so non-root users can read it safely. Exposes the energy counters that are reported via the Running Average Power Limit (RAPL) Model-specific Registers (MSRs) via the hardware monitor (HWMON) sysfs interface.

%prep
%setup -q -c %{name}-master

%files
%doc %{name}-master/README.md
%license %{name}-master/LICENSE

%changelog
{{{ git_dir_changelog }}}
