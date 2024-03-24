%define install_dir %{_libdir}/tlauncher/
%define jar_name tlauncher.jar
%define runner_sh tlauncher.sh
%global srcname tlauncher-copr

Name: tlauncher
Version: 1.0.2
Release: 1%{?dist}
License: Proprietary
Summary: Third-party launcher for Minecraft: Java Edition.
Url: https://tlauncher.org/en
# Sources can be obtained by
# git clone https://github.com/retrozinndev/%{srcname}.git
# cd %{srcname}
# tito build --tgz
Source0: https://github.com/retrozinndev/%{srcname}/archive/refs/tags/v%{version}.tar.gz
BuildArch: noarch

#-- APPLICATION DEPENDENCIES ---------------------------------------------------#
Requires: java-latest-openjdk

#-- BUILD DEPENDENCIES ---------------------------------------------------------#
BuildRequires: wget

%description
TLauncher is a third-party launcher for Minecraft: Java Edition.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build
# Get jar zip
wget https://tlauncher.org/jar
mv jar tl
# Unzip file
unzip tl -x *.txt
mv *.jar tlauncher.jar
# Remove unused zip
rm -rf tl


%install
# copy jar
mkdir -p %{buildroot}%{install_dir}
cp -f %{jar_name} %{buildroot}%{install_dir}
# copy run script
cp -f %{runner_sh} %{buildroot}%{install_dir}
# make binary's symlink in /bin
mkdir -p %{buildroot}%{_bindir}
ln -sf {install_dir}/%{runner_sh} %{buildroot}%{_bindir}/tlauncher


%post
# apply exec permission to runner script
chmod +x %{install_dir}/%{runner_sh} %{_bindir}/%{name}

#-- FILES ---------------------------------------------------------------------#
%files
%doc README.md
%license LICENSE
%{_bindir}/tlauncher
%{install_dir}/*

#-- CHANGELOG -----------------------------------------------------------------#
%changelog

