%global debug_package %{nil}
%global _prj_name certbot-dns-aliyun
%global _install_name certbot_dns_aliyun

Name:           python3-%{_prj_name}
Version:        2.0.0
Release:        5%{?dist}
Summary:        A certbot dns plugin to obtain certificates using aliyun

License:        Apache-2.0
URL:            https://github.com/tengattack/certbot-dns-aliyun
Source0:        %{pypi_source %{_prj_name}}
Patch0:         use-std-mock.patch

BuildRequires:  python3-acme python3-certbot python3-devel python3-pytest python3-setuptools

BuildArch:      noarch

%description
A certbot dns plugin to obtain certificates using aliyun.

%prep
%autosetup -n %{_prj_name}-%{version} -p1

%build
%py3_build

%check
# tests are disabled because many require an API key
#%{__python3} -m pytest

%install
%py3_install

%files -n %{name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{_install_name}/
%{python3_sitelib}/%{_install_name}-%{version}-*.egg-info/

%changelog
* Tue Aug 13 2024 cyqsimon - 2.0.0-5
- Fix installed files declaration

* Tue Aug 13 2024 cyqsimon - 2.0.0-4
- Disable tests due to API key requirement

* Tue Aug 13 2024 cyqsimon - 2.0.0-3
- Use more stable RPM Python macros
  - New ones unavailable in EL8

* Tue Aug 13 2024 cyqsimon - 2.0.0-2
- Add patch to use `unittest.mock` from std

* Tue Aug 13 2024 cyqsimon - 2.0.0-1
- Release 2.0.0
