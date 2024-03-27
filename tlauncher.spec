%define install_dir /usr/lib/tlauncher
%define jar_name tlauncher.jar
%define runner_sh tlauncher.sh
%define update_sh update.sh
%global srcname tlauncher-copr

Name: tlauncher
Version: 1.1.0
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
# copy update script
cp -f %{update_sh} %{buildroot}%{install_dir}

%post
# make runner symlink in /bin
ln -sf %{install_dir}/%{runner_sh} %{_bindir}/%{name}
# make updater symlink in /bin
ln -sf %{install_dir}/%{update_sh} %{_bindir}/tlauncher-update
# apply exec permission to runner script
chmod +x %{install_dir}/%{runner_sh}

#-- FILES ---------------------------------------------------------------------#
%files
%doc README.md
%license LICENSE
%{install_dir}/*

#-- CHANGELOG -----------------------------------------------------------------#
%changelog

