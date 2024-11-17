# Eventos Plus++

Este projeto é um sistema de gerenciamento de eventos desenvolvido com Django para o projeto de finalização do curso FullStack Python do SENAC 2024.2. Ele permite que os organizadores criem e gerenciem eventos, que os usuários se inscrevam em eventos, e inclui funcionalidades como edição de perfil, exportação de inscrições em CSV, entre outras.

## Funcionalidades Principais

- **Visualização de eventos**: Usuários podem ver uma lista de eventos disponíveis.
- **Inscrição em eventos**: Usuários podem se inscrever em eventos.
- **Gerenciamento de eventos por organizadores**: Organizadores podem criar, editar e listar seus próprios eventos.
- **Listagem de participantes**: Organizadores podem visualizar uma lista de participantes de seus eventos.
- **Exportação de dados**: Exportação de inscrições em formato CSV.
- **Edição de perfil**: Usuários podem editar suas informações de perfil.
- **Dashboard Avançado**: Todas as funcionalidades do sistema em um só dashboard dinâmico

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seuusuario/event-management-system.git
   cd event-management-system
   ```

2. **Crie e ative um ambiente virtual**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Realize as migrações**:
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Execute o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```
7. **Adicione o grupo 'Organizadores' e adicione os usuários que organizam os eventos**
   ```bash
   localhost:8000/admin
   ```
   
## Estrutura do Projeto

- **`events`**: App principal que gerencia eventos, inscrições e funcionalidades relacionadas.
- **`users`**: App que gerencia autenticação e edição de perfil de usuários.
- **`templates`**: Contém os templates HTML para renderização das views.
- **`forms.py`**: Define os formulários para registro e edição de usuários.
- **`views.py`**: Contém as views que tratam a lógica do aplicativo.
- **`urls.py`**: Define as rotas para as views.

## Funcionalidades das Views

### `views.py` do App `events`
- **`index(request)`**: Renderiza a página principal.
- **`list_eventos(request)`**: Exibe uma lista de todos os eventos.
- **`list_eventos_organizador(request)`**: Exibe eventos criados pelo organizador atual.
- **`list_detalhes_eventos(request, evento_id)`**: Exibe detalhes de um evento específico.
- **`inscricao_evento(request, evento_id)`**: Permite que um usuário se inscreva em um evento, com verificação de duplicidade.
- **`list_eventos_inscritos(request)`**: Mostra os eventos em que o usuário está inscrito.
- **`apagar_inscricao(request, inscricao_id)`**: Permite que um usuário cancele sua inscrição em um evento.
- **`listar_participantes_evento(request)`**: Exibe uma lista de participantes de eventos do organizador.
- **`exportar_inscricoes_csv(request)`**: Exporta as inscrições em CSV.
- **`inscricao_de_evento(request)`**: Permite a criação de um novo evento por um organizador.
- **`editar_evento(request, evento_id)`**: Permite que um organizador edite detalhes de um evento.

### `views.py` do App `users`
- **`dashboard(request)`**: Exibe um painel com um portal de eventos para usuários e um portal administrativo para organizadores.
- **`editar_usuario(request)`**: Permite que um usuário edite seu perfil.
- **`register_usuario(request)`**: Permite que novos usuários se registrem.

## URLs Principais
- `/` - Página inicial
- `/dashboard/` - Painel de controle dos usuários e dos organizadores
- `/list_eventos/` - Lista de todos os eventos
- `/list_detalhes_eventos/<evento_id>/` - Detalhes de um evento específico
- `/inscricao_evento/<evento_id>/` - Inscrição em um evento
- `/apagar_inscricao/<inscricao_id>/` - Cancelamento de inscrição
- `/exportar-inscricoes/` - Exportação de inscrições em CSV


## Dependências
- **Django**: Framework principal para desenvolvimento web.
- **csv**: Biblioteca usada para exportação de dados em CSV.

## Como Contribuir
1. Faça um fork do repositório.
2. Crie uma branch com sua nova funcionalidade (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Envie para o repositório remoto (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a licença MIT.



