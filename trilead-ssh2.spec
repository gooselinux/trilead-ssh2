Name:           trilead-ssh2
Version:        213
Release:        6.2%{?dist}
Summary:        SSH-2 protocol implementation in pure Java

Group:          Development/Tools
License:        BSD
URL:            http://www.trilead.com/Products/Trilead_SSH_for_Java/
#http://www.trilead.com/DesktopModules/Releases/download_file.aspx?ReleaseId=4102
Source0:        trilead-ssh2-build%{version}.zip
Source1:        build.xml
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  jpackage-utils
BuildRequires:  java-devel
BuildRequires:  ant
Requires:       jpackage-utils
Requires:       java

BuildArch:      noarch

#Obsoletes:              ganymed-ssh2 <= 210


%description
Trilead SSH-2 for Java is a library which implements the SSH-2 protocol in pure
Java (tested on J2SE 1.4.2 and 5.0). It allows one to connect to SSH servers
from within Java programs. It supports SSH sessions (remote command execution
and shell access), local and remote port forwarding, local stream forwarding,
X11 forwarding and SCP. There are no dependencies on any JCE provider, as all
crypto functionality is included.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
Javadoc for trilead-ssh2.

%prep
%setup -q -n %{name}-build%{version}
cp %{SOURCE1} .

# change file encoding
iconv -f ISO-8859-1 -t UTF-8 -o HISTORY.txt HISTORY.txt

# delete the jars that are in the archive
rm %{name}-build%{version}.jar

# fixing wrong-file-end-of-line-encoding warnings
sed -i 's/\r//' LICENSE.txt README.txt HISTORY.txt faq/FAQ.html
find examples -name \*.java -exec sed -i 's/\r//' {} \;

%build
ant


%install
rm -rf $RPM_BUILD_ROOT

# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

pushd $RPM_BUILD_ROOT%{_javadir}/
ln -s %{name}-%{version}.jar %{name}.jar
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_javadir}/*
%doc LICENSE.txt HISTORY.txt README.txt faq examples

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}


%changelog
* Thu Jan 7 2010 Alexander Kurtakov <akurtako@redhat.com> 213-6.2
- Remove gcj_support.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 213-6.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 213-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 30 2009 Robert Marcano <robert@marcanoonline.com> - 213-5
- Fix Bug 492759, bad javadoc package group

* Tue Feb 16 2009 Robert Marcano <robert@marcanoonline.com> - 213-4
- Renaming package because main project moved, based on ganymed-ssh2

