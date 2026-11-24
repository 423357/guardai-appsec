# Fundamentos de segurança

## Conceitos

- **Ativo:** dado, sistema, serviço ou recurso que tem valor e precisa ser protegido.
- **Ameaça:** situação ou agente que pode causar dano a um ativo.
- **Vulnerabilidade:** fraqueza que pode ser explorada ou causar um incidente.
- **Risco:** combinação entre a chance de um evento ocorrer e o impacto que ele teria.

Uma suspeita ainda precisa de evidências. Separe o que foi observado do que é hipótese.

## Tríade CID

- **Confidencialidade:** somente pessoas autorizadas acessam a informação.
- **Integridade:** dados e sistemas permanecem corretos e não são alterados indevidamente.
- **Disponibilidade:** sistemas e informações ficam acessíveis quando necessários.

Ao avaliar impacto, explique qual parte da tríade pode ser afetada e como.

## Boas práticas defensivas

- Conceder somente os acessos necessários e proteger contas administrativas.
- Manter sistema e dependências atualizados.
- Guardar senhas com algoritmos próprios para senhas, como Argon2id, bcrypt ou scrypt; nunca em texto puro.
- Usar consultas parametrizadas para interagir com bancos de dados.
- Manter cópias de segurança e verificar se podem ser restauradas.
- Registrar eventos relevantes e proteger os registros contra acesso ou alteração indevidos.
- Expor somente serviços necessários e revisar suas configurações.
- Testar mudanças em laboratório ou homologação antes de aplicá-las em produção.

## Análise de risco

Considere o ativo afetado, a ameaça, as evidências da vulnerabilidade, o impacto, a probabilidade e as proteções existentes. Classifique a severidade como baixa, média, alta ou crítica e justifique. Quando faltarem dados, deixe a incerteza explícita e diga o que precisa ser confirmado.