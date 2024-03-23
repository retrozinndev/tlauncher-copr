%global srcname tlauncher-copr
%define install_dir %{_libdir}/tlauncher
%define jar_name tlauncher.jar
%define runner_sh tlauncher.sh

Name: TLauncher
Version: 1.0.0
Release: 1%{?dist}
License: Proprietary
Summary: Third-party launcher for Minecraft: Java Edition.
Url: https://tlauncher.org/
# Sources can be obtained by
# git clone https://github.com/retrozinndev/%{srcname}.git
# cd %{srcname}
# tito build --tgz
Source0: https://github.com/retrozinndev/%{srcname}/archive/refs/tags/v%{version}.tar.gz
BuildArch: x86_64

#-- APPLICATION DEPENDENCIES ---------------------------------------------------#
Requires: java-openjdk-latest

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
mv jar tl.zip
# Unzip file
unzip tl.zip
# get the jar out of the unzipped dir
cd tl
mv *.jar ../tlauncher.jar
# Remove unused file/dir
rm -rf tl.zip tl/


%install
# copy jar
mkdir -p %{buildroot}%{install_dir}
cp -f %{jar_name} %{buildroot}%{install_dir}
# copy run script
cp -f %{runner_sh} %{buildroot}%{install_dir}

%post
# make binary's symlink in /bin
ln -sf %{install_dir}/%{runner_sh} %{_bindir}/%{name}
# apply exec permission to runner script
chmod +x %{install_dir}/%{runner_sh}

#-- FILES ---------------------------------------------------------------------#
%files
%doc README.md
%license LICENSE
%{install_dir}/*

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* 1.0.0
- First release of TLauncher Copr Repo!
