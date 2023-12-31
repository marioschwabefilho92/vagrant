Vagrant.configure("2") do |config|
    config.vm.box = "bento/ubuntu-22.04"
    config.vm.synced_folder ".", "/vagrant", disabled: false
    config.vm.synced_folder "C:/vagrant_share", "/media/vagrant_share", create: true

    if Vagrant.has_plugin?("vagrant-timezone")
        config.timezone.value = "Europe/Berlin"
    end

    if Vagrant.has_plugin?("vagrant-disksize")
        config.disksize.size = "100GB"
    end

    config.vm.provider "virtualbox" do |vb|
        vb.name = "Ubuntu 22.04 DEV"
        vb.gui = true
        vb.memory = "16192"
        vb.cpus = 4
        vb.customize ["modifyvm", :id, "--vram", "128"]
        vb.customize ["modifyvm", :id, "--graphicscontroller", "vmsvga"]
        vb.customize ["modifyvm", :id, "--clipboard", "bidirectional"]
    end

    config.vm.provision "Install Ansible", before: :all, type: "shell", inline: <<-SHELL
        apt update
        apt install -y ansible
    SHELL

    config.vm.provision "Run Ansible Playbook", after: :all, type: "ansible_local" do |ansible|
        #ansible.verbose = "v"
        ansible.galaxy_role_file = 'requirements.yml'
        ansible.playbook = "playbook.yml"
        ansible.tags = [ "required", "optional" ]
    end

end
