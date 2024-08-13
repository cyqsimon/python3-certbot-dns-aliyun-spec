%global debug_package %{nil}
%global _prj_name certbot-dns-aliyun
%global _install_name certbot_dns_aliyun

Name:           python3-%{_prj_name}
Version:        2.0.0
Release:        2%{?dist}
Summary:        A certbot dns plugin to obtain certificates using aliyun

License:        Apache-2.0
URL:            https://github.com/tengattack/certbot-dns-aliyun
Source0:        %{pypi_source %{_prj_name}}
Patch0:         use-std-mock.patch

BuildRequires:  python3-devel

BuildArch:      noarch

%description
A certbot dns plugin to obtain certificates using aliyun.

%prep
%autosetup -n %{_prj_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%check
%pyproject_check_import -t

%install
%pyproject_install
%pyproject_save_files %{_install_name}

%files -n %{name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{_install_name}/
%{python3_sitelib}/%{_install_name}*.dist-info/

%changelog
* Tue Aug 13 2024 cyqsimon - 2.0.0-2
- Add patch to use `unittest.mock` from std

* Tue Aug 13 2024 cyqsimon - 2.0.0-1
- Release 2.0.0
